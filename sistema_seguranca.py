#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Segurança Simples
Gerencia autenticação de usuários e monitora tentativas de acesso
"""

import json
import hashlib
import os
from datetime import datetime


class SistemaSeguranca:
    """Classe principal do sistema de segurança"""
    
    def __init__(self):
        self.arquivo_usuarios = "usuarios.json"
        self.arquivo_log = "log_acessos.txt"
        self.usuarios = self.carregar_usuarios()
        self.tentativas_falhas = {}
        self.max_tentativas = 3
    
    def hash_senha(self, senha):
        """Cria um hash SHA-256 da senha"""
        return hashlib.sha256(senha.encode()).hexdigest()
    
    def carregar_usuarios(self):
        """Carrega usuários do arquivo JSON"""
        if os.path.exists(self.arquivo_usuarios):
            try:
                with open(self.arquivo_usuarios, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def salvar_usuarios(self):
        """Salva usuários no arquivo JSON"""
        with open(self.arquivo_usuarios, 'w', encoding='utf-8') as f:
            json.dump(self.usuarios, f, indent=4, ensure_ascii=False)
    
    def registrar_log(self, mensagem):
        """Registra eventos no arquivo de log"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_mensagem = f"[{timestamp}] {mensagem}\n"
        
        with open(self.arquivo_log, 'a', encoding='utf-8') as f:
            f.write(log_mensagem)
        
        print(log_mensagem.strip())
    
    def cadastrar_usuario(self, username, senha):
        """Cadastra um novo usuário"""
        if username in self.usuarios:
            print("❌ Erro: Usuário já existe!")
            return False
        
        if len(senha) < 4:
            print("❌ Erro: Senha deve ter no mínimo 4 caracteres!")
            return False
        
        self.usuarios[username] = {
            "senha_hash": self.hash_senha(senha),
            "bloqueado": False,
            "data_cadastro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.salvar_usuarios()
        self.registrar_log(f"✓ Novo usuário cadastrado: {username}")
        print(f"✓ Usuário '{username}' cadastrado com sucesso!")
        return True
    
    def verificar_bloqueio(self, username):
        """Verifica se o usuário está bloqueado"""
        if username in self.usuarios and self.usuarios[username].get("bloqueado", False):
            return True
        return False
    
    def autenticar(self, username, senha):
        """Autentica um usuário"""
        # Verifica se usuário existe
        if username not in self.usuarios:
            self.registrar_log(f"❌ Tentativa de login falhou: usuário '{username}' não existe")
            print("❌ Usuário ou senha incorretos!")
            return False
        
        # Verifica se está bloqueado
        if self.verificar_bloqueio(username):
            self.registrar_log(f"🚫 Tentativa de acesso bloqueada: {username}")
            print(f"🚫 Usuário '{username}' está bloqueado por excesso de tentativas falhas!")
            return False
        
        # Verifica senha
        senha_hash = self.hash_senha(senha)
        if self.usuarios[username]["senha_hash"] == senha_hash:
            # Login bem-sucedido
            self.tentativas_falhas[username] = 0
            self.registrar_log(f"✓ Login bem-sucedido: {username}")
            print(f"✓ Acesso autorizado! Bem-vindo, {username}!")
            return True
        else:
            # Senha incorreta
            self.tentativas_falhas[username] = self.tentativas_falhas.get(username, 0) + 1
            
            if self.tentativas_falhas[username] >= self.max_tentativas:
                self.usuarios[username]["bloqueado"] = True
                self.salvar_usuarios()
                self.registrar_log(f"🚫 Usuário bloqueado por excesso de tentativas: {username}")
                print(f"🚫 Usuário bloqueado após {self.max_tentativas} tentativas falhas!")
            else:
                tentativas_restantes = self.max_tentativas - self.tentativas_falhas[username]
                self.registrar_log(f"❌ Tentativa de login falhou: {username} (tentativas restantes: {tentativas_restantes})")
                print(f"❌ Senha incorreta! Tentativas restantes: {tentativas_restantes}")
            
            return False
    
    def mostrar_log(self):
        """Exibe o histórico de acessos"""
        if not os.path.exists(self.arquivo_log):
            print("📋 Nenhum registro de acesso encontrado.")
            return
        
        print("\n" + "="*60)
        print("📋 HISTÓRICO DE ACESSOS")
        print("="*60)
        
        with open(self.arquivo_log, 'r', encoding='utf-8') as f:
            logs = f.readlines()
            
        if logs:
            for log in logs[-20:]:  # Mostra últimas 20 entradas
                print(log.strip())
        else:
            print("Nenhum registro encontrado.")
        
        print("="*60 + "\n")
    
    def desbloquear_usuario(self, username):
        """Desbloqueia um usuário (função administrativa)"""
        if username in self.usuarios:
            self.usuarios[username]["bloqueado"] = False
            self.tentativas_falhas[username] = 0
            self.salvar_usuarios()
            self.registrar_log(f"🔓 Usuário desbloqueado: {username}")
            print(f"✓ Usuário '{username}' desbloqueado!")
            return True
        else:
            print(f"❌ Usuário '{username}' não encontrado!")
            return False


def menu_principal():
    """Exibe o menu principal"""
    print("\n" + "="*60)
    print("🔒 SISTEMA DE SEGURANÇA")
    print("="*60)
    print("1. Cadastrar novo usuário")
    print("2. Fazer login")
    print("3. Ver histórico de acessos")
    print("4. Desbloquear usuário (admin)")
    print("5. Sair")
    print("="*60)


def main():
    """Função principal"""
    sistema = SistemaSeguranca()
    
    print("🔒 Bem-vindo ao Sistema de Segurança Simples!")
    
    while True:
        menu_principal()
        
        try:
            opcao = input("\nEscolha uma opção (1-5): ").strip()
            
            if opcao == "1":
                print("\n--- CADASTRAR NOVO USUÁRIO ---")
                username = input("Digite o nome de usuário: ").strip()
                senha = input("Digite a senha: ").strip()
                sistema.cadastrar_usuario(username, senha)
            
            elif opcao == "2":
                print("\n--- LOGIN ---")
                username = input("Usuário: ").strip()
                senha = input("Senha: ").strip()
                sistema.autenticar(username, senha)
            
            elif opcao == "3":
                sistema.mostrar_log()
            
            elif opcao == "4":
                print("\n--- DESBLOQUEAR USUÁRIO ---")
                username = input("Digite o nome do usuário a desbloquear: ").strip()
                sistema.desbloquear_usuario(username)
            
            elif opcao == "5":
                print("\n👋 Encerrando sistema... Até logo!")
                break
            
            else:
                print("❌ Opção inválida! Tente novamente.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Sistema interrompido pelo usuário. Até logo!")
            break
        except Exception as e:
            print(f"❌ Erro: {e}")


if __name__ == "__main__":
    main()

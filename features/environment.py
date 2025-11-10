import sys
import os

def before_all(context):
    # Esta linha encontra o caminho para a pasta raiz do seu projeto
    # (Ex: ~/Desktop/Teste de Sof. - Calculadora)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    # Adiciona a pasta raiz ao 'sys.path'
    sys.path.insert(0, project_root)
    
    # Agora, quando o 'calculadora_steps.py' fizer:
    # 'from src.calculadora import Calculadora'
    # O Python saberá onde encontrar a pasta 'src'.
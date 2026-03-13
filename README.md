# ISL Moon Lander

**Arquivos principais:**
- `main.ipynb`: notebook com código de treino e exemplos de execução.
- [scripts/run_inference.py](scripts/run_inference.py): script para rodar inferência/avaliação sem renderização.
- [scripts/run_render.py](scripts/run_render.py): script para executar o modelo com renderização humana.

**Requisitos (exemplo):**
- Python 3.8+
- gymnasium
- stable-baselines3
- numpy

Recomendado usar um virtualenv ou venv para isolar dependências.

**Instalação rápida:**
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Se não houver `requirements.txt`, instale manualmente:
```bash
pip install gymnasium stable-baselines3 numpy
```

**Treinamento (exemplo):**
- Treine a partir do `main.ipynb` ou adapte o notebook para executar etapas de treino.

**Inferência (avaliar modelo salvo):**
```bash
python scripts/run_inference.py
```

**Render (ver rodando com render humano):**
```bash
python scripts/run_render.py --model ppo_lunarlander --episodes 5
```

**Notas técnicas:**
- O projeto segue as recomendações do Gymnasium para criação do ambiente (`LunarLander-v3`).
- O agente usa `PPO` (Stable Baselines3) e o fluxo de treino/inferência está organizado em notebook e scripts.

**Sobre o trabalho:**
Este repositório foi desenvolvido como parte da disciplina Laboratório de Sistemas Inteligentes. Segui o guia do Gymnasium durante a implementação e o resultado final ficou muito legal — o agente aprendeu a pousar de forma confiável.

**Licença:**
- Sinta-se livre para adaptar este trabalho para fins acadêmicos.

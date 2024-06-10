
#!/bin/bash

if ! [ -x "$(command -v python3)" ]; then
  echo 'Erro: Python 3 não está instalado. Por favor, instale o Python 3 e tente novamente.' >&2
  exit 1
fi

if ! python3 -c "import PIL" &> /dev/null; then
  echo 'Erro: Pillow não está instalado. Por favor, instale o Pillow usando "pip install pillow" e tente novamente.' >&2
  exit 1
fi

cd "$(dirname "$0")" || exit
python3 quiz_ui.py
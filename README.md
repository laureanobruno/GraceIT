# Repositorio de Grace 

## Cómo trabajar solo en este repo

1. Crear un repo
`git init <nombre>`

2. Ir al repo
`cd <nombre>`

3. Añadir el repositorio online
`git remote add -f origin <url>`

4. Habilitar el sparse checkout
`git sparse-checkout init --cone`

5. Setear el directorio a trabajar
`git sparse-checkout set ./Grace`

6. Hacer un pull
`git pull`
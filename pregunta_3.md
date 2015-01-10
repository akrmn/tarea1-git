Pregunta 3
==========

En Git:

* working directory: es el directorio en el cual se está trabajando. Contiene
todos los archivos del proyecto, que están _tracked_, así como otros archivos
que serán ignorados (_untracked_).

* index: también conocido como el _staging area_ incluye todos los cambios que
se han hecho con `git add`. Cuando se está contento con un conjunto de cambios
y se ejecuta `git commit`, los archivos en el _index_ son los que serán
agregados al repositorio local.

* local repo: es el directorio especial (oculto) de git, en el que se
encuentran los distintos commits que han sido realizados con `git commit`. Se
encuentra en la máquina del usuario. Para enviar los cambios al repositorio
remoto se usa `git push`, y para actualizar el repositorio local con los
cambios que podría haber en el remoto se usa `git pull`

* remote repo: es un repositorio que se encuentra en un servidor distinto de la
máquina del usuario, al cual otros usuarios podrían enviar sus propios cambios.
Para facilitar el manejo de repositorios remotos se usa el comando
`git remote add <apodo> <servidor>`, para luego referirse al repositorio remoto
por su apodo.

* dirty working tree: se dice que el directorio de trabajo está _sucio_ cuando
existen archivos _tracked_ que han sido modificados y no han sido agregados al
_index_, o que han sido modificados después de haber sido agregados al _index_.
Una forma de arreglar esto es agregar al index (`git add`) los archivos que han
sido modificados.

* merge conflict: cuando se hace _merge_ de los cambios en un _branch_ en otro
_branch_, es posible que surjan conflictos por haber hecho cambios distintos en
un mismo archivo en cada _branch_. Cuando esto ocurre, git avisa al usuario que
existen conflictos, y los marca de una manera particular en la versión del
archivo que se encuentra en el directorio de trabajo, de forma que puedan ser
resueltos manualmente por el usuario.

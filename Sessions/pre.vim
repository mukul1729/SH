let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/Documents/SH
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
argglobal
%argdel
set stal=2
tabnew
tabnew
tabnew
tabnew
tabnew
tabnew
tabnew
tabnew
tabnew
tabrewind
edit Python/Test/codeforces.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
split
1wincmd k
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe '1resize ' . ((&lines * 25 + 17) / 35)
exe '2resize ' . ((&lines * 6 + 17) / 35)
argglobal
balt OCaml/hello.ml
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 22 - ((21 * winheight(0) + 12) / 25)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 22
normal! 045|
wincmd w
argglobal
if bufexists("term://~/Documents/SH//31649:/bin/bash") | buffer term://~/Documents/SH//31649:/bin/bash | else | edit term://~/Documents/SH//31649:/bin/bash | endif
if &buftype ==# 'terminal'
  silent file term://~/Documents/SH//31649:/bin/bash
endif
balt Python/Test/codeforces.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 6 - ((5 * winheight(0) + 3) / 6)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 6
normal! 0
wincmd w
exe '1resize ' . ((&lines * 25 + 17) / 35)
exe '2resize ' . ((&lines * 6 + 17) / 35)
tabnext
edit Python/Test/new.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 87 + 87) / 174)
exe 'vert 2resize ' . ((&columns * 86 + 87) / 174)
argglobal
balt Python/Test/code.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 16 - ((15 * winheight(0) + 16) / 32)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 16
normal! 0
wincmd w
argglobal
if bufexists("term://~/Documents/SH//2455:/bin/bash") | buffer term://~/Documents/SH//2455:/bin/bash | else | edit term://~/Documents/SH//2455:/bin/bash | endif
if &buftype ==# 'terminal'
  silent file term://~/Documents/SH//2455:/bin/bash
endif
balt Python/Test/new.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 5 - ((4 * winheight(0) + 16) / 32)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 5
normal! 0
wincmd w
exe 'vert 1resize ' . ((&columns * 87 + 87) / 174)
exe 'vert 2resize ' . ((&columns * 86 + 87) / 174)
tabnext
edit Python/Projects/snake.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe '1resize ' . ((&lines * 30 + 17) / 35)
exe 'vert 1resize ' . ((&columns * 173 + 87) / 174)
exe '2resize ' . ((&lines * 30 + 17) / 35)
exe 'vert 2resize ' . ((&columns * 0 + 87) / 174)
argglobal
balt Python/Projects/snake.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 167 - ((28 * winheight(0) + 15) / 30)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 167
normal! 05|
wincmd w
argglobal
if bufexists("term://~/Documents/SH//2576:/bin/bash") | buffer term://~/Documents/SH//2576:/bin/bash | else | edit term://~/Documents/SH//2576:/bin/bash | endif
if &buftype ==# 'terminal'
  silent file term://~/Documents/SH//2576:/bin/bash
endif
balt Python/Projects/snake.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 6 - ((1 * winheight(0) + 15) / 30)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 6
normal! 0
wincmd w
exe '1resize ' . ((&lines * 30 + 17) / 35)
exe 'vert 1resize ' . ((&columns * 173 + 87) / 174)
exe '2resize ' . ((&lines * 30 + 17) / 35)
exe 'vert 2resize ' . ((&columns * 0 + 87) / 174)
tabnext
edit web_dev/HTML/test.html
argglobal
balt web_dev/HTML/test.html
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 4 - ((3 * winheight(0) + 16) / 32)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 4
normal! 09|
tabnext
edit Python/Projects/paint/paint.py
argglobal
balt Python/Projects/paint/paint.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 52 - ((15 * winheight(0) + 16) / 32)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 52
normal! 015|
lcd ~/Documents/SH
tabnext
edit ~/Documents/SH/Lisp/new.lisp
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
split
1wincmd k
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe '1resize ' . ((&lines * 31 + 17) / 35)
exe '2resize ' . ((&lines * 0 + 17) / 35)
argglobal
balt ~/Documents/SH/Lisp/new.lisp
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 1 - ((0 * winheight(0) + 15) / 31)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
wincmd w
argglobal
if bufexists("term://~/Documents/SH//6610:/bin/bash") | buffer term://~/Documents/SH//6610:/bin/bash | else | edit term://~/Documents/SH//6610:/bin/bash | endif
if &buftype ==# 'terminal'
  silent file term://~/Documents/SH//6610:/bin/bash
endif
balt ~/Documents/SH/Lisp/new.lisp
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 5
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 5
normal! 0
wincmd w
exe '1resize ' . ((&lines * 31 + 17) / 35)
exe '2resize ' . ((&lines * 0 + 17) / 35)
tabnext
edit ~/Documents/SH/C/new.c
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
split
1wincmd k
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe '1resize ' . ((&lines * 22 + 17) / 35)
exe '2resize ' . ((&lines * 9 + 17) / 35)
argglobal
balt ~/Documents/SH/C/new.c
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 25 - ((14 * winheight(0) + 11) / 22)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 25
normal! 013|
wincmd w
argglobal
if bufexists("term://~/Documents/SH//5017:/bin/bash") | buffer term://~/Documents/SH//5017:/bin/bash | else | edit term://~/Documents/SH//5017:/bin/bash | endif
if &buftype ==# 'terminal'
  silent file term://~/Documents/SH//5017:/bin/bash
endif
balt ~/Documents/SH/C/new.c
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 127 - ((1 * winheight(0) + 4) / 9)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 127
normal! 0
wincmd w
exe '1resize ' . ((&lines * 22 + 17) / 35)
exe '2resize ' . ((&lines * 9 + 17) / 35)
tabnext
edit ~/Documents/SH/OCaml/helloworld/helloworld.ml
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
split
1wincmd k
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe '1resize ' . ((&lines * 19 + 17) / 35)
exe '2resize ' . ((&lines * 12 + 17) / 35)
argglobal
balt ~/Documents/SH/OCaml/hello.ml
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 2 - ((0 * winheight(0) + 9) / 19)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 2
normal! 0
wincmd w
argglobal
if bufexists("term://~/Documents/SH//6131:/bin/bash") | buffer term://~/Documents/SH//6131:/bin/bash | else | edit term://~/Documents/SH//6131:/bin/bash | endif
if &buftype ==# 'terminal'
  silent file term://~/Documents/SH//6131:/bin/bash
endif
balt ~/Documents/SH/OCaml/hello.ml
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 12 - ((11 * winheight(0) + 6) / 12)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 12
normal! 0
wincmd w
exe '1resize ' . ((&lines * 19 + 17) / 35)
exe '2resize ' . ((&lines * 12 + 17) / 35)
tabnext
edit ~/Documents/SH/D/test.d
argglobal
balt ~/Documents/SH/D/test.d
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 25 - ((20 * winheight(0) + 16) / 32)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 25
normal! 0
tabnext
edit ~/Documents/SH/C\#/Console/Testing/Program.cs
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
split
1wincmd k
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe '1resize ' . ((&lines * 22 + 17) / 35)
exe '2resize ' . ((&lines * 9 + 17) / 35)
argglobal
balt ~/Documents/SH/C\#/Program.cs
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 14 - ((13 * winheight(0) + 11) / 22)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 14
normal! 0
wincmd w
argglobal
if bufexists("term://~/Documents/SH//31262:/bin/bash") | buffer term://~/Documents/SH//31262:/bin/bash | else | edit term://~/Documents/SH//31262:/bin/bash | endif
if &buftype ==# 'terminal'
  silent file term://~/Documents/SH//31262:/bin/bash
endif
balt ~/Documents/SH/C\#/Program.cs
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 9 - ((8 * winheight(0) + 4) / 9)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 9
normal! 0
wincmd w
exe '1resize ' . ((&lines * 22 + 17) / 35)
exe '2resize ' . ((&lines * 9 + 17) / 35)
tabnext 7
set stal=1
badd +1 ~/Documents/SH/Python/Test/codeforces.py
badd +1 ~/Documents/SH/Python/Test/new.py
badd +1 ~/Documents/SH/Python/Projects/snake.py
badd +1 ~/Documents/SH/web_dev/HTML/test.html
badd +1 ~/Documents/SH/Python/Projects/paint/paint.py
badd +1 ~/Documents/SH/Lisp/new.lisp
badd +1 ~/Documents/SH/C/new.c
badd +1 ~/Documents/SH/OCaml/helloworld/helloworld.ml
badd +1 ~/Documents/SH/D/test.d
badd +1 ~/Documents/SH/C\#/Console/Testing/Program.cs
badd +1 ~/Documents/SH/OCaml/hello.ml
badd +1 term://~/Documents/SH//31649:/bin/bash
badd +1 ~/Documents/SH/Python/Test/code.py
badd +1 term://~/Documents/SH//2455:/bin/bash
badd +1 term://~/Documents/SH//2576:/bin/bash
badd +1 term://~/Documents/SH//6610:/bin/bash
badd +1 term://~/Documents/SH//5017:/bin/bash
badd +1 term://~/Documents/SH//6131:/bin/bash
badd +2 ~/Documents/SH/C\#/Program.cs
badd +1 term://~/Documents/SH//31262:/bin/bash
badd +1 ~/Documents/SH/Docker/hello_world/Dockerfile
badd +1 ~/Documents/SH/Python/Pygame/Boxy/Boxy.py
badd +1 ~/Documents/SH/Python/Test/practice/linked_practice.py
badd +1 ~/Documents/SH/Java/ArrayDemo.java
badd +1 ~/Documents/SH/Java/test.java
badd +1 ~/Documents/SH/C++/test.cpp
badd +148 term://~/Documents/SH//2631:/bin/bash
badd +48 ~/.emacs.d/init.el
badd +1 ~/.config/nvim/init.vim
badd +46 ~/Documents/SH/Notes/programs/sorting/quicksort.py
badd +1 ~/Documents/SH/D/project/project
badd +90 ~/Documents/SH/D/project/source/app.d
badd +1 ~/Documents/SH/Python/Pygame/Boxy/images
badd +3 ~/Documents/SH/Notes/todo.txt
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToOF
let &winminheight = s:save_winminheight
let &winminwidth = s:save_winminwidth
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :

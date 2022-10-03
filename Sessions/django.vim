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
badd +1 Python/Projects/django-tutorial/mysite/manage.py
badd +22 Python/Projects/django-tutorial/mysite/mysite/urls.py
badd +0 term://~/Documents/SH//15450:/bin/bash
badd +0 Python/Projects/django-tutorial/mysite/mysite/settings.py
badd +1 Python/Projects/django-tutorial/mysite/polls/views.py
badd +1 Python/Projects/django-tutorial/mysite/polls/urls.py
badd +0 term://~/Documents/SH//15546:/bin/bash
argglobal
%argdel
set stal=2
tabnew
tabnew
tabrewind
edit Python/Projects/django-tutorial/mysite/manage.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
split
wincmd _ | wincmd |
split
2wincmd k
wincmd w
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
exe '1resize ' . ((&lines * 12 + 20) / 40)
exe '2resize ' . ((&lines * 20 + 20) / 40)
exe '3resize ' . ((&lines * 4 + 20) / 40)
argglobal
balt Python/Projects/django-tutorial/mysite/manage.py
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
let s:l = 1 - ((0 * winheight(0) + 6) / 12)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
wincmd w
argglobal
if bufexists("Python/Projects/django-tutorial/mysite/mysite/urls.py") | buffer Python/Projects/django-tutorial/mysite/mysite/urls.py | else | edit Python/Projects/django-tutorial/mysite/mysite/urls.py | endif
if &buftype ==# 'terminal'
  silent file Python/Projects/django-tutorial/mysite/mysite/urls.py
endif
balt Python/Projects/django-tutorial/mysite/manage.py
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
let s:l = 22 - ((18 * winheight(0) + 10) / 20)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 22
normal! 0
wincmd w
argglobal
if bufexists("term://~/Documents/SH//15450:/bin/bash") | buffer term://~/Documents/SH//15450:/bin/bash | else | edit term://~/Documents/SH//15450:/bin/bash | endif
if &buftype ==# 'terminal'
  silent file term://~/Documents/SH//15450:/bin/bash
endif
balt Python/Projects/django-tutorial/mysite/mysite/urls.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 1 - ((0 * winheight(0) + 2) / 4)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
wincmd w
exe '1resize ' . ((&lines * 12 + 20) / 40)
exe '2resize ' . ((&lines * 20 + 20) / 40)
exe '3resize ' . ((&lines * 4 + 20) / 40)
tabnext
edit Python/Projects/django-tutorial/mysite/mysite/settings.py
argglobal
balt Python/Projects/django-tutorial/mysite/mysite/settings.py
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
let s:l = 1 - ((0 * winheight(0) + 18) / 37)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
tabnext
edit Python/Projects/django-tutorial/mysite/polls/views.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
split
wincmd _ | wincmd |
split
2wincmd k
wincmd w
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
exe '1resize ' . ((&lines * 12 + 20) / 40)
exe '2resize ' . ((&lines * 17 + 20) / 40)
exe '3resize ' . ((&lines * 6 + 20) / 40)
argglobal
balt Python/Projects/django-tutorial/mysite/polls/views.py
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
let s:l = 1 - ((0 * winheight(0) + 6) / 12)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
wincmd w
argglobal
if bufexists("Python/Projects/django-tutorial/mysite/polls/urls.py") | buffer Python/Projects/django-tutorial/mysite/polls/urls.py | else | edit Python/Projects/django-tutorial/mysite/polls/urls.py | endif
if &buftype ==# 'terminal'
  silent file Python/Projects/django-tutorial/mysite/polls/urls.py
endif
balt Python/Projects/django-tutorial/mysite/polls/views.py
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
let s:l = 1 - ((0 * winheight(0) + 8) / 17)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
wincmd w
argglobal
if bufexists("term://~/Documents/SH//15546:/bin/bash") | buffer term://~/Documents/SH//15546:/bin/bash | else | edit term://~/Documents/SH//15546:/bin/bash | endif
if &buftype ==# 'terminal'
  silent file term://~/Documents/SH//15546:/bin/bash
endif
balt Python/Projects/django-tutorial/mysite/polls/urls.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 1 - ((0 * winheight(0) + 3) / 6)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
wincmd w
3wincmd w
exe '1resize ' . ((&lines * 12 + 20) / 40)
exe '2resize ' . ((&lines * 17 + 20) / 40)
exe '3resize ' . ((&lines * 6 + 20) / 40)
tabnext 3
set stal=1
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0&& getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
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
set hlsearch
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :

# For setting-up terminal dictionary	
	- pacman -S sdcv		
	- sudo mkdir -p /usr/share/stardict/dic/		
	- [EnglishDict](https://web.archive.org/web/20140428003644/http://abloz.com/huzheng/stardict-dic/dict.org/stardict-dictd_www.dict.org_gcide-2.4.2.tar.bz2)
	- sudo tar -xvjf downloaded.tar.bz2 -C /usr/share/stardict/dic
	- sdcv word

# Useful Terminal Apps
	- pacman -S curseradio (internet radio)
	- pacman -S sdcv	(Dictionary)
	- pacman -S elinks	(Terminal browser)
	- pacman -S cmus	(Terminal Music player)
	- pacman -S cuneiform	(Best ocr reader)
	- pacman -S mutt

# Install Garamond Font
	- sudo wget -P ~/.fonts -A ttf -r -np -nd http://garamond.org/urw/
	- sudo mkfontdir ~/.fonts && xset fp rehash
# Install void packages
	sudo xbps-install --repository=hostdir/binpkgs/nonfree/ steam

# Install dotnet
	mkdir -p $HOME/dotnet && tar zxf dotnet-sdk-3.0.100-linux-x64.tar.gz -C $HOME/dotnet
	export DOTNET_ROOT=$HOME/dotnet
	export PATH=$PATH:$HOME/dotnet






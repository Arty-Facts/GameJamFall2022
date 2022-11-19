# install deps 
sudo apt update
sudo apt install -y\
                cmake\
                libfreetype-dev\
                libgl1-mesa-dev\
                libopenal-dev\
                libsndfile1-dev\
                libudev-dev\
                libvorbis-dev\
                libx11-dev\
                libxrandr-dev\
                libxinerama-dev\
                libsdl2-dev\
                unzip\

### Check if SFML exist  ###
if [ ! -d "SFML" ] 
then
    # Get SFML
    wget -P /tmp https://github.com/SFML/SFML/archive/refs/heads/master.zip
    unzip /tmp/master.zip
    rm /tmp/master.zip
    mv SFML-master SFML
fi


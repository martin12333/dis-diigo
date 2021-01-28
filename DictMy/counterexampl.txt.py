<[^>]*>
	docker build -t xeyes - << __EOF__ FROM debian RUN apt-get update RUN apt-get install -qqy x11-apps ENV DISPLAY :0 CMD xeyes __EOF__ XSOCK=/tmp/.X11-unix XAUTH=/tmp/.docker.xauth xauth nlist :0 | sed -e 's/^..../ffff/' | xauth -f $XAUTH nmerge - docker run -ti -v $XSOCK:$XSOCK -v $XAUTH:$XAUTH -e XAUTHORITY=$XAUTH xeyes 
	wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' sudo apt-get update sudo apt-get install google-chrome-stable




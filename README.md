# ghosts-of-data-past

a ghost from data generator - generates a chat with text messages and selfies from recorded conversations

## background

requires dataset recording, preperation and model finetuning with the following repositories:

- recording a chat between two performers: https://github.com/papayapeter/theater-chat
- preparing chat and mail data and finetuning a gpt-2 model with it: https://github.com/papayapeter/gpt-2-training
- finetuning a stylegan3 model with face images by performers: https://github.com/papayapeter/stylegan3
- generating notification sound abstractions: \_

using [aitextgen](https://github.com/minimaxir/aitextgen) for text generation & [stylegan3](https://github.com/NVlabs/stylegan3). some code has been copies over from the original stylegan3 repo to make image generation and textgeneration work seamlessly together.

## setup

1. to create the envorinment: `conda env create -f environment.yml` or `conda env create -f environment-cpu.yml` for a cpu only version
2. activate the enviroment: `conda activate ghosts` or `conda activate ghosts-cpu`
3. changes to the environment can be saved with: `conda env export --no-builds | grep -v "prefix" > environment.yml`
4. as the site served is built with sveltekit, it's dependencies must be installed and it must be built: `cd serve/site && npm install && npm run build`
5. install redis according to these [instructions](https://redis.io/docs/getting-started/installation/install-redis-on-linux/)

## run

all the steps below should be executed from individual terminals or at least in individual processes

1. start the redis server: `redis-server redis.conf`
2. enter the conda environment: `conda activate ghosts` or `conda activate ghosts-cpu`
3. start the generate script with `python3 generate/generate.py --gptdir=generate/models/gpt2_model --stylegandir=generate/models --prompt=[SCIENTIST:] I can't believe you. --roles=artist,scientist --colors=cyan,green --basetime=3.0 --lettertime=0.2 --imagetime=6.0 --readfactor=0.8 --randomfactor=0.9,1.1` (this is only an example configuration)
4. start the server with `python3 serve/app.py`

## notes & mentions

this repo includes a modified version of [@jsdevtools/rehype-toc](https://github.com/JS-DevTools/rehype-toc). i had to modify it to get it working with mdsvex and put it in the root of this repo as a .tgz file.

## serve - to do

- [x] add keys to svelte each https://svelte.dev/tutorial/keyed-each-blocks
- [x] construct chat bubbles (this might help https://svelte.dev/tutorial/dimensions)
- [x] autoscroll to the bottom https://svelte.dev/tutorial/update (doesn't work with images yet on the desktop) including notifications for new messages if not scrolled to the bottom
- [x] optimize https://svelte.dev/tutorial/svelte-options
- [x] BETTER: pause css animations when not visible https://css-tricks.com/how-to-play-and-pause-css-animations-with-css-custom-properties/, https://abcdinamo.com/news/using-variable-fonts-on-the-web, https://svelte.dev/repl/c461dfe7dbf84998a03fdb30785c27f3?version=3.16.7, https://www.npmjs.com/package/svelte-intersection-observer
- [x] implement soft transitions between pages https://dev.to/evanwinter/page-transitions-with-svelte-kit-35o6
- [x] scroll down on return from about
- [x] change intersection observer for better performance an readability by only adding new elements
- [x] limit the number of chat messages
- [x] decrease the distance between messages from the same sender
- [x] remove the name of messages by the same sender
- [x] implement sidenotes on about
- [x] implement proper menu on about with mute controls
- [x] fix clicking, touching & hovering behaviour on sidenotes (add resize listener, fix clicking vs. hovering, remove clicking behaviour on desktops)
- [x] check, whether socketio.on is triggered after recieving all data
- [x] maybe transfer the font animation to the index page (if it is not used in the about pages)
- [x] check whether the intersection observer works when returning from the abouts page
- [x] add rehype plugin for toc
- [x] fix breathing intersection observers for heading with automatic toc
- [ ] beautify layout for about pages
- [ ] seperate the nav out (one for chat and one for the about pages)
- [ ] donate for pw smokey https://www.dafont.com/pwsmokey.font

## generate - to do

- [x] add redis installation to the setup documentation
- [x] secure redis
- [x] fix saving to redis

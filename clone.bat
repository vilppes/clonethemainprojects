@echo off
cd ..
echo cloning accessibility wiki
git clone https://github.com/vilppes/accessibility-resources
echo cloning bluetooth notes
git clone https://github.com/vilppes/notes-on-learning-bluetooth
echo cloning message sending functionalities library that I made
git clone https://github.com/vilppes/emergency-messaging --branch dev-sm emergency-messaging-devsm
echo cloning profile customization things
git clone https://github.com/vilppes/vilppes
echo cloning cboard
git clone --recursive https://github.com/vilppes/cboard.git
cd cboard
npm install
cd ..
echo cloning the main branch for my own doings on cboard.git
git clone --recursive https://github.com/vilppes/cboard.git --branch dev cboard-dev
cd cboard-dev
npm install
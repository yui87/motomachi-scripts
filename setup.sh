#!/bin/bash
blue=${txtbld}$(tput setaf 4)

mkdir -p motomachi roboto mplus inter
cd inter
wget https://fonts.google.com/download?family=Inter -O inter.zip
unzip inter.zip
cd ../

cd roboto
wget https://fonts.google.com/download?family=Roboto -O roboto.zip
unzip roboto.zip
cd ../

cd mplus
wget https://fonts.google.com/download?family=M+PLUS+1p -O mplus.zip
unzip mplus.zip

echo "${blue}Motomachi を生成するには FontForge をインストールした上で、以下を実行してください。"
echo "${blue}fontforge -lang=py -script motomachi.py"
tput sgr0

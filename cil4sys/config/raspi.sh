#!/bin/bash


echo " uinsatlling previous version of cil4sys package ..."

pip uninstall cil4sys
##
echo "updating system ..."

sudo apt get update
sudo apt upgrade 
##
echo "installing and updating Required lib ... "

sudo pip3 install --upgrade RPi.GPIO
sudo pip3 install--upgrade  RPLCD












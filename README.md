This is a simple/crappy way of fixing FreePBX to allow the use of Mitel 5235 phones.  The issue is that, for some
unknown reason, FreePBX does not have a template for the Mitel 5235 phones.  However, their cfg file is identical
to the 5224 model.  Knowing that allows us to "patch" the cfg files and rename their "Paramater Model=" XML setting to
"5235" instead of "5224".

Each time FreePBX modifies those files (say, adding a button to the phone) it will overwrite our change, so this
program will periodically scan the **/tftpboot** folder and look for cfg files that need re-patched.

In order to NOT change the cfg files of Mitel 5224 phones (if you have some) there is an **excluded_extensions** file
that you can put the filenames of the cfg files you want this program to skip.  Just put one filename per line.

The guy whom I wrote this script for wanted this program to reside in /tftpboot/mitel_patch folder.  You may want to
store this file somewhere else.  If so, modify the **workdir** variable in the script to point to your desired location.

Additionally, I created the systemd service file that you can use to run this script at bootup of the FreePBX server.
Just copy the **mitel_patch.service** file to **/etc/systemd/system/** folder.  Then issue the command
**systemctl enable mitel_patch.service** to configure this file to run at system startup.

Note: You can use the command **journalctl -u mitel_patch** to see the log output.  Currently the log output is sparse
but you can at least see that the program is running and the timestamp it last scanned the files.

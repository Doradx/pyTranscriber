# UPDATE
1. add proxy setting
2. change the function 'pytranscriber.util.MyUtil.is_internet_connected'
3. add requirements.txt

![image](https://user-images.githubusercontent.com/23170065/143678535-750ac415-2be7-41ce-b5c2-f1d319d3e204.png)

# pyTranscriber

pyTranscriber is an application that can be used to generate <b>automatic transcription / automatic subtitles </b> for audio/video files through a friendly graphical user interface. The hard work of speech recognition is made by the <a href="https://cloud.google.com/speech/">Google Speech Recognition API</a> using <a href="https://github.com/agermanidis/autosub">Autosub</a>.
<br>
<br>
![pyTranscriber1](doc/screenshot3.png?raw=true "pyTranscriber")
<br>
[![Watch the video](doc/pyTranscriber.png)](https://youtu.be/DJFpklDnyA4)
<br>
<br>
pyTranscriber is a improved version of my previous project <a href="https://github.com/raryelcostasouza/JAutosub">JAutosub (Java)</a>, created because of the limitations, issues, and overhead of mixing this 2 different languages on a single project.
<br>
<br>
The app by default outputs the subtitles as .srt and the transcribed audio on the user interface as well  as .txt files. SRT Files can be edited using <a href="http://www.aegisub.org/">Aegisub</a>.
Internet connection is REQUIRED because it uses the <a href="https://cloud.google.com/speech/">Google Cloud Speech Server</a> for the job, in the same way as the <a href="https://support.google.com/youtube/answer/6373554?hl=en">Youtube Automatic Subtitles</a>.
<br>
<br>
IMPORTANT: As speech recognition technology is still not fully accurate, the <b>accuracy</b> of the result can vary a lot, depending on many factors, mainly the <b>quality/clarity</b> of the audio. Ideally the audio input should not have background noise, sound effects or music. If there is a single speaker and he speaks in a clear and slow speed seems that the recognition is much more accurate. Sometimes, under ideal/lucky conditions it is possible to get a <a href="https://medium.com/@mlockrey/youtube-s-incredible-95-accuracy-rate-on-auto-generated-captions-b059924765d5">accuracy result close to 95%</a>.
<br>
<br>
![pyTranscriber2](doc/screenshot2.png?raw=true "pyTranscriber")
![pyTranscriber3](doc/screenshot1.png?raw=true "pyTranscriber")
<br>
<br>
<h1>Release Notes:</h1>
<b>07/12/2020 - v1.5 </b>
<br>* Since v1.4.1 COMPATIBLE WITH MACOS CATALINA.
<br>* Upgraded to latest Python and libraries
<br>* Minor GUI tweaks and fixes.
<br><br>
<b>06/12/2020 - v1.4.1:</b>
<br>* Added support for MacOS Catalina!
<br><br>
<b>29/01/2020 - v1.4:</b>
<br>* Fixed crash when exporting txt file for languages with special characters, specially chinese, on Windows system. Thanks for KY Poon for reporting!
<br><br>
<b>18/10/2019 - v1.3:</b>
<br>* Added option for not opening output transcription files automatically after finish
<br>* Fixed bug with canceling during batch processing (only the current job was being stopped... not all of them as expected).
<br><br>
<h1>For Users - Download the Windows/Linux/MacOS portable app</h1>
<a href="https://github.com/raryelcostasouza/pyTranscriber/releases/tag/v1.5-stable"> pyTranscriber-v1.5-stable</a>

<h1> Donations to support the development </h1>
pyTranscriber is developed as a hobby, so donations of any value are welcomed and essential for further improvements.
<br>If you feel that this software has been useful and would like to contribute for it to continue improve and have more features and fixes you can use any of the following donation means:
<br><b><a href="https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=YHB854YHPJCU8&item_name=Donation+pyTranscriber&currency_code=BRL">DONATE VIA PAYPAL</a></b>
<br><b>BITCOIN (bc1qun8q6xsp0pwzyf39qmxt3lpqk6ql458gzlm9u5)</b> or
<br><b>ETHEREUM (0x0db3341579caf72ce972fbbfcdec5cea761538fd)</b>
<br><b>DOGECOIN (DLZ5BMVfhdVxqZKEhcPKX4QuJLrLL42vJC)</b>

<br>Thanks in advance!

<h1>For Developers - Technical Details</h1>
Check at <a href="https://github.com/raryelcostasouza/pyTranscriber/blob/master/doc/technical_details.md">technical_details.md<a>


### License

GPL v3

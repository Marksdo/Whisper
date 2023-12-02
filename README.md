# 🎶 Whisper Mate - Batch local transcribe audio/movie to text with Whisper AI Model. Keep Privacy Safe!




 Download [the latest release from macOS appstore](https://apps.apple.com/us/app/id6450404233)

![screenshot](imgs/appicon-128x128.png)

## Features

Features
Whisper Mate support batch transcribe audio files or movie files into text with OpenAI's Whisper AI Model. With an embed subtitles editor to preview the transcription result segment by segment.   
All transcribe operation is processing in local machine. Keep your privacy safe.   

V5.4.4
---
- Add model cloud list in model config panel with 2 download host support. (Change to host2 if you can't download it in host1)
- Fallback support use CoreML module when disable GPU Accelerate option in general settings
- Fixed download large model fail issue 
- Fixed crash issue on not apple silicon device.
- Download universal edtiton [122 MB](https://download.marksdo.com/apps/WhisperMate/V5.4.4/WhisperMate.zip) 

V5.4.3
---
- Improve transcribe speed
- Add support whisper large v3 model
- Add LibreTranslator engine support
- Add duplicate project in project context menu
- Update speaker field can direct input in edit mode (⌘+E)
- Fixed tabbed window issue when tabbed count > 2
- Fixed waveform view sometime crash issue
- Fixed translate in subtitle editor can't translate selected rows


V5.4.2
---
- Add config whisper process threads count option. (Use less threads let computer to do other jobs, but process time will increase)  
- Add deepgram transcribe engine support, also support in realtime stream transcribe mode.  
- Add template example for export custom speaker content only  
- Add search keyword start with @ to filter speaker rows or replace all speaker name to another name (ex: @tom-->jack)  
- Add feature to save latest project speakers config and reuse in new project.  
- Custom template export add support to 9 custom templates now.

V5.4.1
---
- Add Intranet web remote manage feature, use your phone or other device to add file to process and view processing states (In the main window bottom status bar)
- Add ai parameters config template selector. 
- Add suppress punctuation ai parameter
- Add javascript to use sync http request to get or post data (You can use it to post the subtitle row data to your local llm service to get inference fix result then fill back to origin subtitle, or post to other http/https  system service, load the http example from the javascript processor to see how to use it)
- Fix denoise wav error when file path contain space char

![image](/images/App-Preview-19.webp)

V5.4
---
- Add quick cut feature
- Add shortcut (c) to show or hide subtitle editor preview player
- Add shortcut to change subtitle editor preview player speed
- Replace silent strategy to chunks strategy 
- Fixed denoise option bug
- Download universal edtiton [122 MB](https://download.marksdo.com/apps/WhisperMate/V5.4.4/WhisperMate.zip)

### The new Quick Cut feature has the following functionalities:

- Visualize audio waveform to precisely locate and trim videos.
- Split longer multimedia files into multiple segments for separate processing before transcription.
- Use chunks strategy to skip silent or non-transcribable segments.
- Trim separately the segments that require transcription into individual files.

![image](/images/App-Preview-18.webp)

V5.3.1
---
- Add project priority attribute in batch process queue, higher priority will process first (Option is in  context-menu)
- Subtitle text replace feature also replace matched keyword in translated text
- Fixed Re-transcribe with skip silent strategy & reduce noise issues


V5.3
---
- Add more tuned-models (small/medium) for languages  
- Add transcribe strategy to skip silent segment (classified by decibels & silent duration)  
- Add option to reduce background noise.  
- Add option to make transcribe suppress subtitles show ahead of timestamp (no spoiler).   
- Add example javascript processor to capitalize segment subtitle

V5.2
---
- Add fine-tuned models for difference language inference.  cantonese/zh/ko/jp/de/fr/th/uk...  
- Add feature to add local tuned Whisper AI Model into Whisper Mate.  
- Add feature to batch setup project model parameters  
- Add option to prevent screensaver start when has running queue.  
- Fixed when system screensaver started, processing task paused.  
- Fixed subtitle editor row click sometime can't navigate to player position  
- Fixed subtitle editor modified text undo & redo can't call from context menu  
- Fixed batch export when combine time range not match

V5.1
---
- Add feature to batch export projects segments/srt/template with option to combine into one file  
- Add feature to re-transcribe the selected rows with difference ai parameters  
- Add feature to undo or redo text change in subtitle text content with manual typing change (Shortcuts ⌘+Z undo /  ⌘+⇧+Z redo)  
- Add feature to add new empty subtitle row below selected row (Shortcuts ⌘+N)  
- Add feature to send project finished notification via Slack incoming webhook. (You can get notification on phone when each project transcribe finished)  
- Fixed media play control box location not align center when in Up-Down style layout


V5.0
---
- Add kit to quick auto merge subtitle in consecutive paragraphs  
- Add custom script processor to batch tune the transcribed subtitles  
- Add subtitle editor tune feature. it similar split & merge feature. it can select multi-row then tune them in one textfield line by line  
- Add subtitle editor with more shortcuts support.  
- Add custom font to video preview subtitle style config panel.  
- Add custom font to burn hard subtitle to origin video config panel.  
- Add export support pdf or docx, simple set export suffix to pdf or docx  
- Add more predefined export example format. You can load from example then make an simple tune the template result.  
- Add feature to make snapshots of current project's subtitles state. Then easy recover back to the saved snapshots.  
- Add feature to import .srt to current project as snapshot.  
- Add option to set preview video subtitle display translated text over source text.  
- Add custom export functions. random numbers & random guid & escXML & replaceString with custom format  
- Add custom export output type (file or clipboard)  
- Add custom export option on use all subtitles to export or only the selected  
- Add project editor window group with main window option  
- Add extra whisper model process parameters config in model selector (in bottom-right corner), may be not easy to find. Cause most case do not need to modify these parameters  
- Optimize fullscreen preview video behaviors  
- Search keyword support or condition (use | to as the or keyword . ex "hi|hello|hey")  
- Optimize the search & replace logic. When replace exec do search keywords will tune to show src keywords & replaced keywords  
- Optimize realtime stream transcribe logic  
- Fixed some sub window do not bring to front issue  
- Fixed export xml format some bugs  
- Fixed some media extract wav fail   
- Fixed leave replace keyword field will auto fired replace action issue  
- Fixed stream project some crash issue


V4.0
---
- Add feature to remember the project subtitle editor's layout properties. Each project can use difference layout and preview player size.(old project need to open again then will remember the layout properties)
- Add option to find duplicated subtitle in editor
- Add context menu option to open editor even transcribe script process not start
- Add export subtitles to .sbv format
- Add custom export templates features (like .fcpxml, .itt, .ttml)
- Add new plugin 
- Add frequently use keywords & replace config option for quick reuse search or replace
- Add marked row show an Mark flag in preview player's progress view
- Add mark option in subtitle editor context menu
- Add split row feature in subtitle editor when select single row
- Add search result show project name in row
- Add show error info when pre-progress media encounter error
- Add option to hide editor locate row button
- Add ⌘+S shortcut to quick export .srt to file
- Fixed media channel audio meta info get two audio channel but in fact one. (add option to ignore audio channel select)
- Fixed burn subtitle fail when project name has manual changed
- Fixed some UI issues on macOS12
- Fixed stay on feature not lock show status bar icon option
- Fixed some light theme UI display issues

## V3.5 Features
- Add subtitles audio clip download feature. Now you can select any subtitles then use context menu to download it's audio clip, when selected multi-rows, it will auto merge into one audio clip.
- Add tiny floating window style for realtime capture audio
- Add Menubar context menu can quick start record stream to project with new floating window
- Add quick play segment row range audio in global search result or direct download the search result audio range clip 
- Add Models download now support breakpoint resume
- Add subtitle memo features, now you can add memo to any subtitle in the editor
- Add azure translate option
- Add global subtitle search in all projects
- Add highlight search keywords in search result
- Add default shortcuts for quick control window like Close/Zoom/Minimize
- Add option to hide main toolbar's label
- Changed Batch start button move from the main toolbar to context menu
- Fixed replace can't replace with empty string
- Fixed missing small & small-en models in backup servers
- Fixed recorded audio file player's slider location subtitle issue



## Features  

- Transcribe audio or video files   
- Support capture and transcribe audio in other app like (Zoom/Skype/Teams/Other App, macOS13.0+ Only & need Screen Recording Permission)   
- Use DeepL free api translate subtitles  
- Embed subtitle editor to fix transcription  
- Export to SRT,VTT,CSV,JSON,SEGMENT  
- Support set speaker to each subtitle  
- Most operation support batch select to invoke. Like batch task run. batch rows translate. batch rows set speaker  
- Support drag and drop files to start transcription  
- Support typing on search transcript  
- Editor can preview audio or video file sync the playing range  
- Dxport selected subtitles's media range to an new media clip file  
- Dxport video with burn hard subtitles to the original video & custom subtitle style  
- Direct preview subtitle inside video preview (subtitle style can be custom in preference panel)  
- Record microphone audio and support realtime transcribe (macOS13+)  
- Subtitle merge features. Segment range & subtitle will merge into one row.  
- Record app audio will auto save to file and can be turn it into an new transcribe project.  
- Duplicate subtitle row and allow modify it's content or time range to fine tune full subtitles  
- Support media preview replay speed custom  
- Support ⌘+V to paste copied files to process queue  
- Cpu usage percent display when whisper processing   
- Support archive projects by context menu (Keep working project list clean)  
- Support google translate in subtitles translate control  
- Full size preview media with subtitle layout  
- Support open media files inside finder's open with features  
- Support multi-language convert  
- Support custom frequently use language for convert or translate

## Screenshots

![screenshot](imgs/App-Preview-1.webp)

![screenshot1](imgs/App-Preview-2.webp)

![screenshot2](imgs/App-Preview-3.webp)

![screenshot3](imgs/App-Preview-4.webp)

![screenshot4](imgs/App-Preview-5.webp)

![screenshot5](imgs/App-Preview-6.webp)

![screenshot6](imgs/App-Preview-7.webp)

![screenshot7](imgs/App-Preview-8.webp)

![screenshot8](imgs/App-Preview-9.webp)

![screenshot10](imgs/App-Preview-10.webp)

![screenshot11](imgs/App-Preview-11.webp)

![screenshot12](imgs/App-Preview-12.webp)

![screenshot13](imgs/App-Preview-13.webp)

![screenshot14](imgs/App-Preview-14.webp)

![screenshot15](imgs/App-Preview-15.webp)

![screenshot16](imgs/App-Preview-16.webp)
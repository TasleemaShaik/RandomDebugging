**Some Useful Debugging #1**
- **Initially, when I tried to run without setting required environment variables as per [README.md prerequisites instructions](https://github.com/adrg/libvlc-go/wiki/Install-on-Windows) silly me** 

    ```$ go run onlineExamWithADistraction.go 
    # github.com/adrg/libvlc-go/v3
    ..\..\..\..\go\pkg\mod\github.com\adrg\libvlc-go\v3@v3.1.6\av.go:4:11: fatal error: vlc/vlc.h: No such file or directory
        4 | // #include <vlc/vlc.h>
        |           ^~~~~~~~~~~
    compilation terminated.
    ```

- **Next, As per instructions, I did download the SDK and set it in the path**
    ```
    $ export CGO_LDFLAGS="-L/c/Users/<USER>/Downloads/VideoLAN.LibVLC.Windows.3.0.21/build/x64"
    $ export CGO_CFLAGS="-I/c/Users/<USER>/Downloads/VideoLAN.LibVLC.Windows.3.0.21/build/x64/include"
    ```
    Then I got this error
    ```
    C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: can
    not find -lvlc: No such file or directory
    ```

    Trace Log
    ```
    $ go build
    # onlineExamWithADistraction
    C:\Program Files\Go\pkg\tool\windows_amd64\link.exe: running gcc failed: exit status 1
    C:\msys64\mingw64\bin\gcc.exe -m64 -mconsole -Wl,--tsaware -Wl,--nxcompat -Wl,--major-os-version=6 -Wl,--minor-os-version=1 -Wl,--major-subsystem-version=6 -Wl,--minor-subsystem-version=1 -Wl,--dynamicbase -Wl,--high-entropy-va -o $WORK\b001\exe\a.out.exe -Wl,--no-insert-timestamp C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\go.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000000.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000001.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000002.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000003.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000004.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000005.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000006.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000007.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000008.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000009.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000010.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000011.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000012.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000013.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000014.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000015.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000016.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000017.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000018.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000019.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000020.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000021.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000022.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000023.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000024.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000025.o C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\000026.o -LC:/Users/SUNYLoaner/Downloads/VideoLAN.LibVLC.Windows.3.0.21/build/x64/lib -lvlc -lvlc -lvlc -lvlc -lvlc -lvlc -lvlc -lvlc -lvlc -lvlc -lvlc -lvlc -lvlc -lvlc -lvlc -lvlc -lvlc -LC:/Users/SUNYLoaner/Downloads/VideoLAN.LibVLC.Windows.3.0.21/build/x64/lib -Wl,-T,C:\Users\<USER>\AppData\Local\Temp\go-link-3802378270\fix_debug_gdb_scripts.ld -Wl,--start-group -lmingwex -lmingw32 -Wl,--end-group -lkernel32
    C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lvlc: No such file or directory 
    C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lvlc: No such file or directory 
    C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lvlc: No such file or directory 
    C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lvlc: No such file or directory 
    C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lvlc: No such file or directory 
    C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lvlc: No such file or directory 
    C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lvlc: No such file or directory 
    C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lvlc: No such file or directory 
    C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lvlc: No such file or directory 
    C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lvlc: No such file or directory 
    C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lvlc: No such file or directory 
    C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lvlc: No such file or directory 
    C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lvlc: No such file or directory 
    C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lvlc: No such file or directory 
    C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lvlc: No such file or directory 
    C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lvlc: No such file or directory 
    C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/14.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: can
    not find -lvlc: No such file or directory 
    collect2.exe: error: ld returned 1 exit status
    ```

- **Linking Errors & Missing Import Libraries:**  
  I finally figured out why this was happening....It is because the VLC NuGet package provided only DLLs (and a .lib file) that weren't directly usable by MinGW. This meant it needed proper MinGW‑compatible import libraries (like libvlc.dll.a).

- **Extracting Exported symbols from the DLL using dumpbin:**  
  I have used dumpbin to extract exported symbols from the DLLs.
  ```
  "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.43.34808\bin\Hostx86\arm\dumpbin.exe" /EXPORTS "C:\Users\<USER>\Downloads\VideoLAN.LibVLC.Windows.3.0.21\build\x64\lib\libvlc.dll" > libvlc_exports.txt
  "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.43.34808\bin\Hostx86\arm\dumpbin.exe" /EXPORTS "C:\Users\SUNYLoaner\Downloads\VideoLAN.LibVLC.Windows.3.0.21\build\x64\lib\libvlccore.dll" > libvlccore_exports.txt
  ```
    Please find the exports output files here:
    [libvlc_exports.txt](exports-files/libvlc_exports.txt)

    [libvlccore_exports.txt](exports-files/libvlccore_exports.txt)


- **Generating DEF Files:**
    To create a DEF file listing all the exported symbols manually was risky and could cause inaccuracy, So I wrote a small Python script to parse the dumpbin output and generate a DEF file automatically.
    ```
    Usage: 
    $ python generate_def.py input_exports.txt output.def
    DEF file generated with 764 symbols and written to output.def
    ```
    Please find the python script used to generate DEF files and the generated DEF files here:
    [generate-def.py](python-script/generate-def.py)

    [libvlc.def](DEF-Files/libvlc.def)

    [libvlccore.def](DEF-Files/libvlccore.def)

- **Creating Import Libraries with dlltool:**  
  Once the DEF files are ready, I ran dlltool to generate import libraries from the DEF files. These import libraries are something GCC (MinGW) can link against when we use the -lvlc flag.
  ```
  dlltool -D libvlc.dll -d libvlc.def -l libvlc.dll.a
  dlltool -D libvlccore.dll -d libvlccore.def -l libvlccore.dll.a
  ```
  For this, I didn't have to set any this binary is automatically found in Mingw's installation
  ```
  $ which dlltool
  /c/msys64/mingw64/bin/dlltool
  ```

- **Setting Up Environment Variables:**  
  I updated the `CGO_CFLAGS` and `CGO_LDFLAGS` to point to the correct VLC SDK include directory and to the directory containing the generated import libraries, which finally resolved the linking errors.
  [EnvAndOutput.sh](env/EnvAndOutput.sh)

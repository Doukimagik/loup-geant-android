import os, shutil
mf = "android/app/src/main/AndroidManifest.xml"
s = open(mf, encoding="utf-8").read()
perms = ["ACCESS_FINE_LOCATION", "ACCESS_COARSE_LOCATION", "ACCESS_BACKGROUND_LOCATION",
         "FOREGROUND_SERVICE", "FOREGROUND_SERVICE_LOCATION", "POST_NOTIFICATIONS"]
add = "".join('    <uses-permission android:name="android.permission.%s" />\n' % p for p in perms)
s = s.replace("</manifest>", add + "</manifest>")
open(mf, "w", encoding="utf-8").write(s)
if os.path.isdir("res"):
    shutil.copytree("res", "android/app/src/main/res", dirs_exist_ok=True)
print("patch ok")

# tju_unipus

tju_unipus是由滑稽盾采紫由（HJDCZY）开发的一个大英u校园自动化小工具。可以节省同学们的时间，提高效率。
本工具使用chrome和chromedriver开发，在release包中我们包含了chrome和chromedriver，而源代码因github不能上传大于100MB的文件，所以我们没有上传chrome。
我在release中上传的是chorme-win64,如果你的系统不是win64，请自行下载对应的chrome。

**注意：本工具只能完成填空题，剩下的题请自行完成**

## 使用方法

<details>

<summary>如果您使用的是v0.0.1版本</summary>
1. 安装python3.7及以上版本。

2. 在release页面下载v0.0.1版本的`tju_unipus.zip`并解压。

3. 将`config.py.example`重命名为`config.py`，用任意编辑器打开`config.py`，按照注释填写内容，将内容填写在引号之间。
 - 对于`user.name`和`user.password`，分别填写你的大英u校园账号和密码。
 - 对于`user.chormelocation`，进入chrome-win64文件夹，填写`chrome.exe`的绝对路径。
 - 对于`user.chromedriverlocation`，进入chromedriver-win64文件夹，填写`chromedriver.exe`的绝对路径。
 - 例如：
 ```python
 user.chormelocation = r"D:\code\unipus\tju_unipus\chrome-win64\chrome.exe"
user.chormedriverlocation = r"D:\code\unipus\tju_unipus\chromedriver-win64\chromedriver.exe"
```

4. 右键unipus.py-打开方式，用python打开

5. 运行后，程序会自动打开chrome并自动登录u校园，请手动跳过u校园环境检测，点进任意一个练习的界面并停留。

6. 完成第5步后，在弹出的cmd界面（黑色窗口）按一下回车（里面也会提示你）

7. 静待你的u校园自动完成

8. 完成后，按enter退出

</details>

<details>
<summary>如果您使用的是v0.0.2版本</summary>

1. 在release页面下载v0.0.2版本的`tju_unipus.zip`并解压。

2. 补充config.ini文件，填写你的大英u校园账号和密码，以及chrome和chromedriver的路径。
    - 对于`chormelocation`，进入chrome-win64文件夹，填写`chrome.exe`的绝对路径。
    - 对于`chromedriverlocation`，进入chromedriver-win64文件夹，填写`chromedriver.exe`的绝对路径。
    注意不要加引号，正确的格式可以是
    ```ini
    chormelocation = D:\code\unipus\tju_unipus\chrome-win64\chrome.exe
    chormedriverlocation = D:\code\unipus\tju_unipus\chromedriver-win64\chromedriver.exe
    ```

3. 运行unipus4.exe

4. 运行后，程序会自动打开chrome并自动登录u校园，请手动跳过u校园环境检测，点进任意一个练习的界面并停留。

5. 完成第5步后，在弹出的cmd界面（黑色窗口）按一下回车（里面也会提示你）

6. 静待你的u校园自动完成

7. 完成后，按enter退出

## 注意事项

在程序进行的时候，有时候可能会出现进入新页面不动的情况，那是因为程序在等待
```
本单元学习时间：无限制

是否必修：必修

确定
```
这个框的出现，5秒等不到就把答案填上，所以你不用管，让它超时就可以。

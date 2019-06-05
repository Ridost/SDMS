# main_style.css基本使用方法

## 基礎模板
```html
{% extends 'AS/base.html' %}

{% block title %}{% endblock %}

{% block script %}{% endblock %}

{% block article %}
    <h1>登入</h1>
    <hr class="heading">
{% endblock %}

{% block topbar %}{% endblock %}

{% block navbar %}{% endblock %}

{% block sidebar %}
    <ul>
        <li><a href="" class="sidebar-item"></a></li>
    </ul>
{% endblock %}
```

|block|用途|
|-|-|
|title|內容決定本頁面的標題名稱。通常來說會寫`宿舍管理系統 - (頁面名稱)`。|
|script|用於插入JS腳本的區塊。一般狀況下留空，但也可依據網頁狀況添加。|
|article|網頁主要區塊的內容。基本最需要編輯的地方。|
|topbar|主畫面的橫幅圖片。只有index會用到，其餘頁面直接留空。|
|navbar|切換四個子系統的橫幅導引大標籤。通常狀況下，會在自己的子系統另外寫一個navbar.html並include在這裡（因為對於同一個子系統而言，這部分都是一樣的。）|
|sidebar|側邊欄功能選單。在各子系統內容大致相同，但需要根據頁面更改class標籤。|



## navbar.html
```html
<a href="/DMS/main/" class="navbar-item">宿舍管理</a>
<a href="/DLS/main/" class="navbar-item">宿舍生活</a>
<a href="/RS/main/" class="navbar-item">問題回報</a>
<a href="/AS/main/" class="navbar-item">會員專區</a>
```
注意，不管你在哪個子系統，**你都不需要更改這四個標籤的順序**。它們會自己排列好。

複製一份，然後將自己子系統那一行的class改為`navbar-item-selected`即可。完成之後，利用`{% include 檔案位置 %}`方法放到你的html頁面中。



## block article 說明
```html
<h1>本頁標題</h1>
<hr class="heading">
```
幾乎所有的`article`頁面都會使用這個做開頭（極少數是例外）。標題內的頁面名稱要填得和`title`的頁面名稱相同，以求一致性。

*注意：*你不需要在你的article裡寫入任何與登入、登出功能相關的東西。這些都已經被包含在基礎模板內了。



## block sidebar 說明
```html
<ul>
    <li><a href="/AS/main/" class="sidebar-item-selected">會員基本資料</a></li>
    <li><a href="/AS/modify/" class="sidebar-item">修改基本資料</a></li>
    <li><a href="/AS/logout/" class="sidebar-item">登出系統</a></li>
    <li><a href="/AS/test/" class="sidebar-item">測試</a></li>
</ul>
```
此處以AS子系統為例。

`href`標籤內放入連結，然後在每個html內把相對應的`class`標籤內改成`sidebar-item-selected`即可。本例是取自會員基本資料的頁面，所以該標籤為selected。



## CSS基本注意事項

- 因為本CSS設計上的問題，你幾乎不可能用到html內的`id`屬性。最多最多就是使用到`class`屬性，所以請把`id`屬性全部刪除。
- 可以自行添加`style`屬性。這是自由的，只是出現外觀衝突大概只有你自己能處理。
- 請不要添加修改字體的屬性。
- 需要什麼東西直接講直接問，我想辦法弄給你。



## 通用class語法標籤

以下的內容是在編寫`block article`時可能會需要的東西，對於基本排版會有幫助。

- button物件

|class|content|
|-|-|
|button-accept|黃色按鈕。一般用於確認、送出等功能。|
|button-decline|灰色按鈕。一般用於取消等功能，或是很多不同功能集結在同一畫面時使用的按鈕。|
|button-warning|紅色按鈕。用於需要注意，或是不該被誤觸的功能。|

- table物件

|class|content|
|-|-|
|(留空)|一般用在兩欄式的表格，可以顯示例如會員基本資料的東西。因為帶有min-width屬性，所以不能用在多欄表格上。|
|vertical|用在很多列的表格，例如清單之類的。表格寬度會依據內容大小自動調整。|

- input物件

|class|content|
|-|-|
|normal-input|用在不需要確認內容，或是填不填都無所謂的欄位。|
|check-input|用在需要確認內容的必填項（例如帳號密碼）。|











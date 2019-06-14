# SDMS
- django==2.0.5
- all db model in AS
- user: admin pwd: ggininder30cm
- [宿舍管理系統需求分析規格書](https://docs.google.com/document/d/1e4HUTmRYDU0zfzpa5FRnCo6pT7ENsX0ncKWby8rSg88/edit)

## git management
- use your own branch
- use rebase to merge and test, before push to master branch
- [Git official book](https://git-scm.com/book/zh-tw/v2)
- [Git-Tutorials GIT基本使用教學](https://github.com/twtrubiks/Git-Tutorials)
- [Resources to learn Git](https://try.github.io/)

### some git commends which commonly used
> - "AS" is a branch forked by "master"
> - So... replace "master" as the branch you forked by
> - So... replace "AS" as your branch

- pull and rebase
  - purpose: 下載master和更新自己的branch
  1. **git checkout master**(切換到master)
  2. **git pull**(pull master的更新)
  3. **git checkout AS**(切換到AS)
  4. **git rebase master**(從master rebase到AS)

- rebase and push
  - purpose: 把最新的master上傳
  1. **git rebase master**(從master rebase到AS)
  2. **git checkout master**(切換到master)
  3. **git merge AS**(merge AS to master)
  4. **git push**(push更新)

- reset
  - purpose: 回到某一個commit
  1. **git reset abcde**
  > "abcde" is a commit hash number which you want to reset

### db sync SOP
- just update model.py file
  1. modfiy model.py and **python manage.py makemigrations**(產生migrate文件，但是還沒有更改db)
  2. commit(新增一個還原點)
  3. **python manage.py migrate**(更改db)
  4. test model.py(到後台查看更動是否正確，並測試新增資料功能)
  5. if test passed -> reset(回復到step 2的還原點)
  6. rebase and push

- insert some data to db
  1. pull and rebase
  2. commit(新增一個還原點)
  3. **python manage.py migrate**(更改db)
  4. insert your data
  5. if not successed -> reset(回復到step 2的還原點) and don't push -> db sync error
  6. rebase and push

## python
- [Python Naming Styles](https://realpython.com/python-pep8/#naming-conventions)

## django tutorial
- django 2.0
  - [Djagno official doc](https://docs.djangoproject.com/zh-hans/2.0/)
  - [IMU-web example](https://github.com/tratitude/IMU-web)
  - [BridgeMaster web example](https://github.com/tratitude/BridgeMaster/tree/master/Web)
  - [django.contrib.auth.models.User](https://docs.djangoproject.com/en/2.0/ref/contrib/auth/#django.contrib.auth.models.User)

- django 1.0 (legacy, just see how it works)
  - [MDN doc](https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django)
  - [Django 基本教學 - 從無到有 Django-Beginners-Guide](https://github.com/twtrubiks/django-tutorial)

- diagram generator
  - [Using django-extensions to visualize the database diagram in django application](https://medium.com/@yathomasi1/1-using-django-extensions-to-visualize-the-database-diagram-in-django-application-c5fa7e710e16)
  - [GraphvizOnline](https://dreampuf.github.io/GraphvizOnline/)
  - [The sitemap framework](https://docs.djangoproject.com/en/2.0/ref/contrib/sitemaps/)
  
## web design
- bootstrap
  - [django-bootstrap4 0.0.8 official](https://pypi.org/project/django-bootstrap4/)
  - [Django搭建个人博客：使用 Bootstrap 4 改写模板文件](https://segmentfault.com/a/1190000016459726)
  - [Bootstrap official](https://getbootstrap.com/)

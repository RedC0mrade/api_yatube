WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
----------------------- Проверка flake8 пройдена -----------------------

============================= test session starts ==============================
platform linux -- Python 3.9.16, pytest-6.2.4, py-1.11.0, pluggy-0.13.1 -- /usr/local/bin/python
django: settings: yatube_api.settings (from env)
rootdir: /app, configfile: pytest.ini, testpaths: tests/
plugins: django-4.4.0, pythonpath-0.7.3
collecting ... collected 55 items

tests/test_comment.py::TestCommentAPI::test_comments_not_authenticated ERROR [  1%]
tests/test_comment.py::TestCommentAPI::test_comment_single_not_authenticated ERROR [  3%]
tests/test_comment.py::TestCommentAPI::test_comments_not_found ERROR     [  5%]
tests/test_comment.py::TestCommentAPI::test_comments_id_available ERROR  [  7%]
tests/test_comment.py::TestCommentAPI::test_comments_get ERROR           [  9%]
tests/test_comment.py::TestCommentAPI::test_comment_create_by_unauth ERROR [ 10%]
tests/test_comment.py::TestCommentAPI::test_comments_post_auth_with_valid_data ERROR [ 12%]
tests/test_comment.py::TestCommentAPI::test_comments_auth_post_with_invalid_data ERROR [ 14%]
tests/test_comment.py::TestCommentAPI::test_comment_author_and_post_are_read_only ERROR [ 16%]
tests/test_comment.py::TestCommentAPI::test_comment_id_auth_get ERROR    [ 18%]
tests/test_comment.py::TestCommentAPI::test_comment_change_by_auth_with_valid_data[put] ERROR [ 20%]
tests/test_comment.py::TestCommentAPI::test_comment_change_by_auth_with_valid_data[patch] ERROR [ 21%]
tests/test_comment.py::TestCommentAPI::test_comment_change_not_auth_with_valid_data[put] ERROR [ 23%]
tests/test_comment.py::TestCommentAPI::test_comment_change_not_auth_with_valid_data[patch] ERROR [ 25%]
tests/test_comment.py::TestCommentAPI::test_comment_delete_by_author ERROR [ 27%]
tests/test_comment.py::TestCommentAPI::test_comment_delete_by_not_author ERROR [ 29%]
tests/test_comment.py::TestCommentAPI::test_comment_delete_by_unauth ERROR [ 30%]
tests/test_follow.py::TestFollowAPI::test_follow_not_found ERROR         [ 32%]
tests/test_follow.py::TestFollowAPI::test_follow_not_auth ERROR          [ 34%]
tests/test_follow.py::TestFollowAPI::test_follow_get ERROR               [ 36%]
tests/test_follow.py::TestFollowAPI::test_follow_create ERROR            [ 38%]
tests/test_follow.py::TestFollowAPI::test_follow_search_filter ERROR     [ 40%]
tests/test_group.py::TestGroupAPI::test_group_not_found ERROR            [ 41%]
tests/test_group.py::TestGroupAPI::test_group_list_not_auth ERROR        [ 43%]
tests/test_group.py::TestGroupAPI::test_group_page_not_found ERROR       [ 45%]
tests/test_group.py::TestGroupAPI::test_group_single_not_auth ERROR      [ 47%]
tests/test_group.py::TestGroupAPI::test_group_auth_get ERROR             [ 49%]
tests/test_group.py::TestGroupAPI::test_group_create ERROR               [ 50%]
tests/test_group.py::TestGroupAPI::test_group_page_auth_get ERROR        [ 52%]
tests/test_jwt.py::TestJWT::test_jwt_create__invalid_request_data ERROR  [ 54%]
tests/test_jwt.py::TestJWT::test_jwt_create__valid_request_data ERROR    [ 56%]
tests/test_jwt.py::TestJWT::test_jwt_refresh__invalid_request_data ERROR [ 58%]
tests/test_jwt.py::TestJWT::test_jwt_refresh__valid_request_data ERROR   [ 60%]
tests/test_jwt.py::TestJWT::test_jwt_verify__invalid_request_data ERROR  [ 61%]
tests/test_jwt.py::TestJWT::test_jwt_verify__valid_request_data ERROR    [ 63%]
tests/test_post.py::TestPostAPI::test_post_not_found ERROR               [ 65%]
tests/test_post.py::TestPostAPI::test_post_list_not_auth ERROR           [ 67%]
tests/test_post.py::TestPostAPI::test_post_single_not_auth ERROR         [ 69%]
tests/test_post.py::TestPostAPI::test_posts_auth_get ERROR               [ 70%]
tests/test_post.py::TestPostAPI::test_posts_get_paginated ERROR          [ 72%]
tests/test_post.py::TestPostAPI::test_post_create_auth_with_invalid_data ERROR [ 74%]
tests/test_post.py::TestPostAPI::test_post_create_auth_with_valid_data ERROR [ 76%]
tests/test_post.py::TestPostAPI::test_post_unauth_create ERROR           [ 78%]
tests/test_post.py::TestPostAPI::test_post_get_current ERROR             [ 80%]
tests/test_post.py::TestPostAPI::test_post_change_auth_with_valid_data[put] ERROR [ 81%]
tests/test_post.py::TestPostAPI::test_post_change_auth_with_valid_data[patch] ERROR [ 83%]
tests/test_post.py::TestPostAPI::test_post_change_not_auth_with_valid_data[put] ERROR [ 85%]
tests/test_post.py::TestPostAPI::test_post_change_not_auth_with_valid_data[patch] ERROR [ 87%]
tests/test_post.py::TestPostAPI::test_post_change_not_author_with_valid_data[put] ERROR [ 89%]
tests/test_post.py::TestPostAPI::test_post_change_not_author_with_valid_data[patch] ERROR [ 90%]
tests/test_post.py::TestPostAPI::test_post_patch_auth_with_invalid_data[put] ERROR [ 92%]
tests/test_post.py::TestPostAPI::test_post_patch_auth_with_invalid_data[patch] ERROR [ 94%]
tests/test_post.py::TestPostAPI::test_post_delete_by_author ERROR        [ 96%]
tests/test_post.py::TestPostAPI::test_post_delete_not_author ERROR       [ 98%]
tests/test_post.py::TestPostAPI::test_post_unauth_delete_current ERROR   [100%]

==================================== ERRORS ====================================
_______ ERROR at setup of TestCommentAPI.test_comments_not_authenticated _______
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
---------------------------- Captured stdout setup -----------------------------
Operations to perform:
  Synchronize unmigrated apps: api, djoser, messages, rest_framework, staticfiles
  Apply all migrations: admin, auth, contenttypes, posts, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying posts.0001_initial... OK
  Applying sessions.0001_initial... OK
---------------------------- Captured stderr setup -----------------------------
Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
____ ERROR at setup of TestCommentAPI.test_comment_single_not_authenticated ____
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
___________ ERROR at setup of TestCommentAPI.test_comments_not_found ___________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
_________ ERROR at setup of TestCommentAPI.test_comments_id_available __________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
______________ ERROR at setup of TestCommentAPI.test_comments_get ______________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
________ ERROR at setup of TestCommentAPI.test_comment_create_by_unauth ________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
___ ERROR at setup of TestCommentAPI.test_comments_post_auth_with_valid_data ___
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
__ ERROR at setup of TestCommentAPI.test_comments_auth_post_with_invalid_data __
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
_ ERROR at setup of TestCommentAPI.test_comment_author_and_post_are_read_only __
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
__________ ERROR at setup of TestCommentAPI.test_comment_id_auth_get ___________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
_ ERROR at setup of TestCommentAPI.test_comment_change_by_auth_with_valid_data[put] _
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
_ ERROR at setup of TestCommentAPI.test_comment_change_by_auth_with_valid_data[patch] _
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
_ ERROR at setup of TestCommentAPI.test_comment_change_not_auth_with_valid_data[put] _
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
_ ERROR at setup of TestCommentAPI.test_comment_change_not_auth_with_valid_data[patch] _
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
________ ERROR at setup of TestCommentAPI.test_comment_delete_by_author ________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
______ ERROR at setup of TestCommentAPI.test_comment_delete_by_not_author ______
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
________ ERROR at setup of TestCommentAPI.test_comment_delete_by_unauth ________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
____________ ERROR at setup of TestFollowAPI.test_follow_not_found _____________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
_____________ ERROR at setup of TestFollowAPI.test_follow_not_auth _____________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
_______________ ERROR at setup of TestFollowAPI.test_follow_get ________________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
______________ ERROR at setup of TestFollowAPI.test_follow_create ______________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
__________ ERROR at setup of TestFollowAPI.test_follow_search_filter ___________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
_____________ ERROR at setup of TestGroupAPI.test_group_not_found ______________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
___________ ERROR at setup of TestGroupAPI.test_group_list_not_auth ____________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
___________ ERROR at setup of TestGroupAPI.test_group_page_not_found ___________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
__________ ERROR at setup of TestGroupAPI.test_group_single_not_auth ___________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
______________ ERROR at setup of TestGroupAPI.test_group_auth_get ______________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
_______________ ERROR at setup of TestGroupAPI.test_group_create _______________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
___________ ERROR at setup of TestGroupAPI.test_group_page_auth_get ____________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
_______ ERROR at setup of TestJWT.test_jwt_create__invalid_request_data ________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
________ ERROR at setup of TestJWT.test_jwt_create__valid_request_data _________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
_______ ERROR at setup of TestJWT.test_jwt_refresh__invalid_request_data _______
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
________ ERROR at setup of TestJWT.test_jwt_refresh__valid_request_data ________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
_______ ERROR at setup of TestJWT.test_jwt_verify__invalid_request_data ________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
________ ERROR at setup of TestJWT.test_jwt_verify__valid_request_data _________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
______________ ERROR at setup of TestPostAPI.test_post_not_found _______________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
____________ ERROR at setup of TestPostAPI.test_post_list_not_auth _____________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
___________ ERROR at setup of TestPostAPI.test_post_single_not_auth ____________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
______________ ERROR at setup of TestPostAPI.test_posts_auth_get _______________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
____________ ERROR at setup of TestPostAPI.test_posts_get_paginated ____________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
____ ERROR at setup of TestPostAPI.test_post_create_auth_with_invalid_data _____
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
_____ ERROR at setup of TestPostAPI.test_post_create_auth_with_valid_data ______
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
____________ ERROR at setup of TestPostAPI.test_post_unauth_create _____________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
_____________ ERROR at setup of TestPostAPI.test_post_get_current ______________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
___ ERROR at setup of TestPostAPI.test_post_change_auth_with_valid_data[put] ___
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
__ ERROR at setup of TestPostAPI.test_post_change_auth_with_valid_data[patch] __
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
_ ERROR at setup of TestPostAPI.test_post_change_not_auth_with_valid_data[put] _
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
_ ERROR at setup of TestPostAPI.test_post_change_not_auth_with_valid_data[patch] _
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
_ ERROR at setup of TestPostAPI.test_post_change_not_author_with_valid_data[put] _
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
_ ERROR at setup of TestPostAPI.test_post_change_not_author_with_valid_data[patch] _
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
__ ERROR at setup of TestPostAPI.test_post_patch_auth_with_invalid_data[put] ___
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
_ ERROR at setup of TestPostAPI.test_post_patch_auth_with_invalid_data[patch] __
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
___________ ERROR at setup of TestPostAPI.test_post_delete_by_author ___________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
__________ ERROR at setup of TestPostAPI.test_post_delete_not_author ___________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
________ ERROR at setup of TestPostAPI.test_post_unauth_delete_current _________
E   sqlite3.OperationalError: no such table: posts_group

The above exception was the direct cause of the following exception:
E   django.db.utils.OperationalError: no such table: posts_group
=========================== short test summary info ============================
ERROR tests/test_comment.py::TestCommentAPI::test_comments_not_authenticated
ERROR tests/test_comment.py::TestCommentAPI::test_comment_single_not_authenticated
ERROR tests/test_comment.py::TestCommentAPI::test_comments_not_found - django...
ERROR tests/test_comment.py::TestCommentAPI::test_comments_id_available - dja...
ERROR tests/test_comment.py::TestCommentAPI::test_comments_get - django.db.ut...
ERROR tests/test_comment.py::TestCommentAPI::test_comment_create_by_unauth - ...
ERROR tests/test_comment.py::TestCommentAPI::test_comments_post_auth_with_valid_data
ERROR tests/test_comment.py::TestCommentAPI::test_comments_auth_post_with_invalid_data
ERROR tests/test_comment.py::TestCommentAPI::test_comment_author_and_post_are_read_only
ERROR tests/test_comment.py::TestCommentAPI::test_comment_id_auth_get - djang...
ERROR tests/test_comment.py::TestCommentAPI::test_comment_change_by_auth_with_valid_data[put]
ERROR tests/test_comment.py::TestCommentAPI::test_comment_change_by_auth_with_valid_data[patch]
ERROR tests/test_comment.py::TestCommentAPI::test_comment_change_not_auth_with_valid_data[put]
ERROR tests/test_comment.py::TestCommentAPI::test_comment_change_not_auth_with_valid_data[patch]
ERROR tests/test_comment.py::TestCommentAPI::test_comment_delete_by_author - ...
ERROR tests/test_comment.py::TestCommentAPI::test_comment_delete_by_not_author
ERROR tests/test_comment.py::TestCommentAPI::test_comment_delete_by_unauth - ...
ERROR tests/test_follow.py::TestFollowAPI::test_follow_not_found - django.db....
ERROR tests/test_follow.py::TestFollowAPI::test_follow_not_auth - django.db.u...
ERROR tests/test_follow.py::TestFollowAPI::test_follow_get - django.db.utils....
ERROR tests/test_follow.py::TestFollowAPI::test_follow_create - django.db.uti...
ERROR tests/test_follow.py::TestFollowAPI::test_follow_search_filter - django...
ERROR tests/test_group.py::TestGroupAPI::test_group_not_found - django.db.uti...
ERROR tests/test_group.py::TestGroupAPI::test_group_list_not_auth - django.db...
ERROR tests/test_group.py::TestGroupAPI::test_group_page_not_found - django.d...
ERROR tests/test_group.py::TestGroupAPI::test_group_single_not_auth - django....
ERROR tests/test_group.py::TestGroupAPI::test_group_auth_get - django.db.util...
ERROR tests/test_group.py::TestGroupAPI::test_group_create - django.db.utils....
ERROR tests/test_group.py::TestGroupAPI::test_group_page_auth_get - django.db...
ERROR tests/test_jwt.py::TestJWT::test_jwt_create__invalid_request_data - dja...
ERROR tests/test_jwt.py::TestJWT::test_jwt_create__valid_request_data - djang...
ERROR tests/test_jwt.py::TestJWT::test_jwt_refresh__invalid_request_data - dj...
ERROR tests/test_jwt.py::TestJWT::test_jwt_refresh__valid_request_data - djan...
ERROR tests/test_jwt.py::TestJWT::test_jwt_verify__invalid_request_data - dja...
ERROR tests/test_jwt.py::TestJWT::test_jwt_verify__valid_request_data - djang...
ERROR tests/test_post.py::TestPostAPI::test_post_not_found - django.db.utils....
ERROR tests/test_post.py::TestPostAPI::test_post_list_not_auth - django.db.ut...
ERROR tests/test_post.py::TestPostAPI::test_post_single_not_auth - django.db....
ERROR tests/test_post.py::TestPostAPI::test_posts_auth_get - django.db.utils....
ERROR tests/test_post.py::TestPostAPI::test_posts_get_paginated - django.db.u...
ERROR tests/test_post.py::TestPostAPI::test_post_create_auth_with_invalid_data
ERROR tests/test_post.py::TestPostAPI::test_post_create_auth_with_valid_data
ERROR tests/test_post.py::TestPostAPI::test_post_unauth_create - django.db.ut...
ERROR tests/test_post.py::TestPostAPI::test_post_get_current - django.db.util...
ERROR tests/test_post.py::TestPostAPI::test_post_change_auth_with_valid_data[put]
ERROR tests/test_post.py::TestPostAPI::test_post_change_auth_with_valid_data[patch]
ERROR tests/test_post.py::TestPostAPI::test_post_change_not_auth_with_valid_data[put]
ERROR tests/test_post.py::TestPostAPI::test_post_change_not_auth_with_valid_data[patch]
ERROR tests/test_post.py::TestPostAPI::test_post_change_not_author_with_valid_data[put]
ERROR tests/test_post.py::TestPostAPI::test_post_change_not_author_with_valid_data[patch]
ERROR tests/test_post.py::TestPostAPI::test_post_patch_auth_with_invalid_data[put]
ERROR tests/test_post.py::TestPostAPI::test_post_patch_auth_with_invalid_data[patch]
ERROR tests/test_post.py::TestPostAPI::test_post_delete_by_author - django.db...
ERROR tests/test_post.py::TestPostAPI::test_post_delete_not_author - django.d...
ERROR tests/test_post.py::TestPostAPI::test_post_unauth_delete_current - djan...
============================== 55 errors in 0.78s ==============================
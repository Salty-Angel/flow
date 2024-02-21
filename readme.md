To run:

requirements:
`pip install django`

`$> python manage.py shell`
`>>> from init_demo import *`


Available users -> role:
- raistlin ->  Warlock
- goldmoon ->  Cleric
- gandolf ->  Admin
- gary ->  DM

Actions
 - do_task(pk, user)
     Mark a task as completed
 - finish_phase(pk, user)
     Mark a phase as completed
 - print_project(proj)
     Show the project as a tree
 - status(proj)
     Show info about project
 - reset(proj)
     Reset the completion status of the project




Example:
```
>>> status(proj)

-- Current Phase --
   [4] QA

-- Log --
   [5/7] completed.


   [ 1] Initialize Project   completed by Goldmoon    on 2024-02-21 16:07:11.025488+00:00.
   [ 2] Write Code           completed by Goldmoon    on 2024-02-21 16:07:44.750923+00:00.
   [ 9] Staging              completed by Goldmoon    on 2024-02-21 16:08:53.513450+00:00.
   [10] Production           completed by Gandolf     on 2024-02-21 16:09:30.167293+00:00.
   [ 3] Deploy               completed by Raistlin    on 2024-02-21 16:10:26.681302+00:00.


>>> finish_phase(4, goldmoon)
"QA" completed by Goldmoon at 2024-02-21 16:10:58.241318+00:00.
>>> print_project(proj)



 ✅ [PHASE] <1> Initialize Project
         ✅ [TASK] <6> Git init
 ✅ [PHASE] <2> Write Code
 ✅ [PHASE] <3> Deploy
         ✅ [PHASE] <9> Staging
                 ✅ [TASK] <11> Build Image
                 ✅ [TASK] <12> Staging Argo
         ✅ [PHASE] <10> Production
                 ✅ [TASK] <11> Build Image
                 ✅ [TASK] <13> Prod Argo
 ✅ [PHASE] <4> QA
         ❌ [TASK] <7> Check for bugs
         ❌ [TASK] <8> Looks Beautiful
 ❌ [PHASE] <5> Profit
```

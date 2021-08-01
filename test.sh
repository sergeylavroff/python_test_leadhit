#!/bin/bash

curl -X POST -d 'first_name=anything&last_name=something&tellno=+79009991112&birthday=10.08.1965' http://127.0.0.1:8088/get-form
#expected: birthday

curl -X POST -d 'first_name=anything&last_name=something&tellno=+79009991112&birthday=10.08.1965&celebrate=yes' http://127.0.0.1:8088/get-form
#expected: birthday

curl -X POST -d 'first_name=anything&last_name=something&owner=+79009991112&made=10.08.1965&color=blue' http://127.0.0.1:8088/get-form
#expected: carregistry

curl -X POST -d 'owner=+79009991112&made=10.08.1965&color=blue' http://127.0.0.1:8088/get-form
#expercted: fields

curl -X POST -d 'work_tel=+79009991112&cell=+79009991112&first_name=10.08.1965&last_name=blue' http://127.0.0.1:8088/get-form
#expected: fields

curl -X POST -d 'work_tel=+79009991112&cell=+79009991112&first_name=abyrvalg&last_name=blue' http://127.0.0.1:8088/get-form
#expected: phonebook
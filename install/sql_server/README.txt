/*
This directory serves two purposes:

1. During development, it provides a quick way to get the database into a known state
2. As a last resort, if the Caliper SDK does not provide a DbObject that serves your
   purpose for interacting with the database, these can be used to install
   updates into the Q2 datacenter (with the caveats listed below).

You can include any SQL files you want in this folder.
Any files in this directory will be run by the `q2 run_sql` command
in alphabetical order, so we recommend a naming convention such as:

01 - Setup.sql
02 - PopulateData.sql
03 - CreateUsers.sql
...

You may run the `q2 run_sql` command yourself and provide other credentials
to test on your own database.

These will **NOT** be run automatically against any stacks in the Q2 datacenter.
They must be installed by a Q2 employee.

We recommend the use of DbObjects, which are described both in the
online documentation and at the end of the tutorial. These are imported from
q2_sdk.hq.db.*

**This SQL will be reviewed before installation into production.**
*/

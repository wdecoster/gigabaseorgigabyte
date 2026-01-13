---
title: "Adding a progress bar to albacore"
date: 2017-05-02T14:24:37
draft: false
categories: ["Nanopore"]
---

Albacore is software from Oxford Nanopore Technologies to perform basecalling of the reads obtained by their sequencers. Since the wrapper script is written in Python I can adapt it, and I wanted to try to add a progress bar to the script and that turned out to be surprisingly easy. Obviously, there was no need to reinvent the wheel, and a suitable Python library ([progressbar2](https://pypi.python.org/pypi/progressbar2)) already exists. The result is shown in the screenshot below:

![ProgressBar-example](/gigabaseorgigabyte/images/2017-04_progressbar-example.jpg)

This module can conveniently be installed using pip:

pip install progressbar2

If you have multiple python versions installed, make sure to use the right (Python3) pip executable, preferably using the following:

python3 -m pip install progressbar2

Since Albacore is proprietary software I cannot disclose the full code here below, but it shouldn't be a problem to replicate my changes. I would suggest to copy the original script (called read_fast5_basecaller.py) and make changes in the copy. Adding the progress bar involves adding just a few extra lines. Note that whenever a new version of the tool becomes available you'll have to make the same changes again.

Important: I don't have rights to the software and all changes you make are your own responsibility. I don't claim this will work on each system and/or produce desirable results. Use at your own risk.

I hope my explanation on what you have to change will be understandable for both Pythonistas and novice programmers. If something is unclear, please leave a comment and I'll clarify further.

First, add the import statement at the top of the script with the other import statements, on a separate line. The order of imports doesn't matter.
import progressbar
Next, in the process_pipeline() function you have to add the progress bar as a "context wrapper". Just above the while loop you add
with progressbar.ProgressBar(max_value=num_files) as bar:
Pay attention to the indentation, which is crucial in Python. The rest of the lines of this function below our newly added line needs to be indented with another tab. This is about 65 lines which need another tab in front of them. As such you indicate that those lines 'belong to the context manager' we added.

Finally, just below the line file_index += 1 you add another line (on the same indentation level):
bar.update(file_index)
That's all!
__author__ = "Dohoon Lee"
__copyright__ = "Copyright 2018, Dohoon Lee"
__email__ = "dohlee.bioinfo@gmail.com"
__license__ = "MIT"

import sys
from os import path

from snakemake.shell import shell

def optionify_input(parameter, option):
    """Return optionified parameter."""
    try:
        return option + ' ' + snakemake.input[parameter]
    except AttributeError:
        return ''

def optionify_params(parameter, option):
    """Return optionified parameter."""
    try:
        return option + ' ' + snakemake.params[parameter]
    except AttributeError:
        return ''

# Extract log.
log = snakemake.log_fmt_shell(stdout=False, stderr=True)
# Extract parameters.
java_options = '--java-options ' + snakemake.params.get('java_options', '-Xmx4g')

# Extract required arguments.
input_command = ' '.join('-I ' + file for file in snakemake.input)
output = snakemake.output[0]

# Extract optional arguments
extra = snakemake.params.get('extra', '')
if '--annotated-intervals' not in extra:
    annotated_intervals = optionify_input('annotated_intervals', '--annotated-intervals')
else:
    annotated_intervals = ''

# Execute shell command.
shell(
    "("
    "gatk "
    "{java_options} "
    "CreateReadCountPanelOfNormals "
    "{input_command} "
    "--output {output} "
    "{annotated_intervals} "
    "{extra} "
    ")"
    "{log}"
)

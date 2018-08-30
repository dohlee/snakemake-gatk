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
input = snakemake.input.count_file
standardized_cr = snakemake.output.standardized_copy_ratios
denoised_cr = snakemake.output.denoised_copy_ratios

# Extract optional arguments
extra = snakemake.params.get('extra', '')
if '--annotated-intervals' not in extra:
    annotated_intervals_option = optionify_input('annotated_intervals', '--annotated-intervals')
else:
    annotated_intervals_option = ''

if '--count-panel-of-normals' not in extra:
    count_pon_option = optionify_input('count_panel_of_normals', '--count-panel-of-normals')
else:
    count_pon_option = ''

# Execute shell command.
shell(
    "("
    "gatk "
    "{java_options} "
    "DenoiseReadCounts "
    "--input {input} "
    "{annotated_intervals_option} "
    "{count_pon_option} "
    "--standardized-copy-ratios {standardized_cr} "
    "--denoised-copy-ratios {denoised_cr} "
    "{extra} "
    ")"
    "{log}"
)

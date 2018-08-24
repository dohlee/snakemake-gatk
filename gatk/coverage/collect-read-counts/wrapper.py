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
bam = snakemake.input.bam
interval_list = snakemake.input.interval_list
output = snakemake.output[0]

# Extract optional arguments
extra = snakemake.params.get('extra', '')
if '--interval-merging-rule' not in extra and '-imr' not in extra:
    interval_merging_rule_option = optionify_params('interval_merging_rule', '--interval-merging-rule')
else:
    interval_merging_rule_option = ''

# Execute shell command.
shell(
    "("
    "gatk "
    "{java_options} "
    "CollectReadCounts "
    "--input {bam} "
    "--intervals {interval_list} "
    "--output {output} "
    "{interval_merging_rule_option} "
    "{extra} "
    ")"
    "{log}"
)

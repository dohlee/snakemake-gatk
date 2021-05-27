__author__ = "Dohoon Lee"
__copyright__ = "Copyright 2021, Dohoon Lee"
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
extra = snakemake.params.get('extra', '')
java_options = '--java-options ' + snakemake.params.get('java_options', '-Xmx16g')

read_group_library = optionify_params('read_group_library', '--RGLB')
read_group_platform = optionify_params('read_group_platform', '--RGPL')
read_group_platform_unit = optionify_params('read_group_platform_unit', '--RGPU')
read_group_sample_name = optionify_params('read_group_sample_name', '--RGSM')

# Extract required input arguments.
input_bam = snakemake.input[0]

# Extract output
output_bam = snakemake.output[0]

# Execute shell command.
shell(
    "("
    "gatk "
    "{java_options} "
    "AddOrReplaceReadGroups "
    "--INPUT {input_bam} "
    "--OUTPUT {output_bam} "
    "{extra} "
    "{read_group_library} "
    "{read_group_platform} "
    "{read_group_platform_unit} "
    "{read_group_sample_name} "
    ")"
    "{log}"
)

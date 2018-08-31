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
vcf = snakemake.input.vcf
output = snakemake.output[0]

# Extract optional arguments
extra = snakemake.params.get('extra', '')
select_type_to_include_option = optionify_params('select_type_to_include', '--select-type-to-include')
select_type_to_exclude_option = optionify_params('select_type_to_exclude', '--select-type-to-exclude')
restrict_alleles_to_option = optionify_params('restrict_alleles_to', '--restrict-alleles-to')
intervals_option = optionify_params('intervals', '--intervals')
params = [
    extra,
    select_type_to_include_option,
    select_type_to_exclude_option,
    restrict_alleles_to_option,
    intervals_option
]

assert not all([param == '' for param in params]), 'You should specify some parameters!'

# Execute shell command.
shell(
    "("
    "gatk "
    "{java_options} "
    "SelectVariants "
    "--variant {vcf} "
    "{select_type_to_include_option} "
    "{select_type_to_exclude_option} "
    "{restrict_alleles_to_option} "
    "{intervals_option} "
    "--output {output} "
    "{extra} "
    ")"
    "{log}"
)

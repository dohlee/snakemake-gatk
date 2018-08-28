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
extra = snakemake.params.get('extra', '')
java_options = '--java-options ' + snakemake.params.get('java_options', '-Xmx16g')

# Extract required input arguments.
bam = snakemake.input.bam
common_biallelic_variants = snakemake.input.common_biallelic_variants

interval_option = ''
if '-L' not in extra and '--intervals' not in extra:
    interval_option = '--intervals %s' % common_biallelic_variants

# Extract output
output = snakemake.output[0]

# Execute shell command.
shell(
    "("
    "gatk "
    "{java_options} "
    "GetPileupSummaries "
    "{extra} "
    "--input {bam} "
    "--variant {common_biallelic_variants} "
    "{interval_option} "
    "--output {output} "
    ")"
    "{log}"
)

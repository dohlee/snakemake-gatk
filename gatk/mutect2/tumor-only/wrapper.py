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
java_options = '--java-options ' + snakemake.params.get('java_options', '-Xmx64g')
sample_name = snakemake.params.get('sample_name', path.basename(path.splitext(path.basename(snakemake.input.bam))[0]))

# Extract required input arguments.
reference = snakemake.input.reference
bam = snakemake.input.bam

# Extract optional input arguments.
germline_resource_option = ''
if '--germline-resource' not in extra:
    germline_resource_option = optionify_input('germline_resource', '--germline-resource')

# Extract parameters.
# NOTE: This option is decided to be included by default according to the article
# https://gatkforums.broadinstitute.org/gatk/discussion/11136
if '--disable-read-filter' not in extra and '-DF' not in extra:
    extra += ' --disable-read-filter MateOnSameContigOrNoMappedMateReadFilter'

# Extract output
output = snakemake.output[0]

# Execute shell command.
shell(
    "("
    "gatk "
    "{java_options} "
    "Mutect2 "
    "--reference {reference} "
    "--input {bam} "
    "-tumor {sample_name} "
    "{germline_resource_option} "
    "--output {output} "
    ")"
    "{log}"
)

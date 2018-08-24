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
tumor_sample_name = snakemake.params.get('tumor_sample_name', path.splitext(path.basename(snakemake.input.tumor))[0])
normal_sample_name = snakemake.params.get('normal_sample_name', path.splitext(path.basename(snakemake.input.normal))[0])

# Extract required input arguments.
reference = snakemake.input.reference
tumor_bam = snakemake.input.tumor
normal_bam = snakemake.input.normal

# Extract optional input arguments.
germline_resource_option = ''
if '--germline-resource' not in extra:
    germline_resource_option = optionify_input('germline_resource', '--germline-resource')

panel_of_normals_option = ''
if '--panel-of-normals' not in extra and '-pon' not in extra:
    panel_of_normals_option = optionify_input('panel_of_normals', '--panel-of-normals')

# Extract parameters.
# NOTE: This option is decided to be included by default according to the article
# https://gatkforums.broadinstitute.org/gatk/discussion/11136
if ('--disable-read-filter' not in extra) and ('-DF' not in extra):
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
    "--input {tumor_bam} "
    "-tumor {tumor_sample_name} "
    "--input {normal_bam} "
    "-normal {normal_sample_name} "
    "{germline_resource_option} "
    "{panel_of_normals_option} "
    "--output {output} "
    "{extra} "
    ")"
    "{log}"
)

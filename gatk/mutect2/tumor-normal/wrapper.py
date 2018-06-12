__author__ = "Dohoon Lee"
__copyright__ = "Copyright 2018, Dohoon Lee"
__email__ = "dohlee.bioinfo@gmail.com"
__license__ = "MIT"

import sys
from os import path

from snakemake.shell import shell

# Extract log.
log = snakemake.log_fmt_shell(stdout=False, stderr=True)
# Extract parameters.
extra = snakemake.params.get('extra', '')
java_options = '--java-options ' + snakemake.params.get('java_options', '-Xmx4g')
germline_resource = '--germline-resource ' + snakemake.params.germline_resource if 'germline_resource' in snakemake.params else ''
tumor_sample_name = snakemake.params.get('tumor_sample_name', 'tumor')
normal_sample_name = snakemake.params.get('normal_sample_name', 'normal')

# Extract required arguments.
reference = snakemake.input.reference
tumor_bam = snakemake.input.tumor
normal_bam = snakemake.input.normal
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
    "{germline_resource} "
    "--output {output}"
    ")"
    "{log}"
)

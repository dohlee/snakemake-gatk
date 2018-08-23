__author__ = "Dohoon Lee"
__copyright__ = "Copyright 2018, Dohoon Lee"
__email__ = "dohlee.bioinfo@gmail.com"
__license__ = "MIT"


from os import path

from snakemake.shell import shell

# Extract log.
log = snakemake.log_fmt_shell(stdout=False, stderr=True)
# Extract parameters.
extra = snakemake.params.get('extra', '')
java_options = '--java-options ' + snakemake.params.get('java_options', '-Xmx32g')

# Extract required arguments.
input = snakemake.input[0]
output = snakemake.output[0]
assert len(snakemake.output) < 3, 'MarkDuplicates generates at most two output files.'

if len(snakemake.output) == 2:
    metrics_command = '--METRICS_FILE %s ' % snakemake.output[1]
else:
    metrics_command = ''

# Too many file handles may throw an error.
# The maximum number of opened file handles can be checked through `ulimit -n` command.
if 'MAX_FILE_HANDLES' not in extra:
    extra += ' -MAX_FILE_HANDLES 2000'

# Execute shell command.
shell(
    "("
    "gatk "
    "{java_options} "
    "MarkDuplicates "
    "--INPUT {input} "
    "--OUTPUT {output} "
    "{metrics_command} "
    "{extra}"
    ")"
    "{log}"
)

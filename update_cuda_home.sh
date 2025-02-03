# Conda environment activation/deactivation to manage CUDA_HOME
update_cuda_home() {
    if [[ -n "$CONDA_PREFIX" ]]; then
        export CUDA_HOME="$CONDA_PREFIX"
        export PATH=$CONDA_PREFIX/bin:$PATH
        export LD_LIBRARY_PATH="$CUDA_HOME/lib:$LD_LIBRARY_PATH"
    else
        unset CUDA_HOME  # Unset when no environment is active
    fi
}

# Ensure the update function is called every time the shell prompt changes
export PROMPT_COMMAND="update_cuda_home; $PROMPT_COMMAND"

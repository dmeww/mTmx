# mTmx
A tool to execute some install-scripts without docker environment

## Usage
### 1. Bundle 
use `bun build src/index.ts` to compile, and you will get a binary executable file.

### 2. Use
You will need to provide a URL which is a list of json called repo

Inside the repo, it needs contain some infomations to describe the `pkg` and its install-script


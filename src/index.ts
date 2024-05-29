import * as p from '@clack/prompts';
import listPackages from "./list";
import {updateRepo} from "./update";
import {config} from "./data";

const todos = [
    'list',
    'update',
    'dir'
]

async function main() {
    console.clear()
    let args = Bun.argv.slice(2, Bun.argv.length);
    p.intro(`[ My-Tmx ]`)
    if (!args.length) {
        p.outro(`Usage: [ ${todos.join(' , ')} ]`)
        return
    }

    let [action, param] = args

    switch (action) {
        case 'update': {
            if (param) {
                p.log.info(`Updating Repo from: ${param}`)
                await updateRepo(param)
                p.log.success('Updated')
            } else
                p.log.error('Error: Not RepoURL Specified')
            break
        }
        case 'list': {
            await listPackages()
            break
        }
        case 'dir':{
            p.log.success(`Home-Dir:=> [ ${config.home}/ ]`)
            p.log.success(`Repo-Location:=> [ ${config.home}/repo.json ]`)
            p.log.success(`Temp-Dir:=> [ ${config.tmp}/ ]`)
            break
        }
        default: {
            p.outro(`Usage: my-tmx [ list | update URL ]`)
        }
    }


}

main().catch(console.error)
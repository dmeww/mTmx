import type {Pkg} from "../types";
import * as p from '@clack/prompts'
import {config} from "../data";

export default async (pkg: Pkg) => {
    const spin = p.spinner()

    spin.start('Pulling...')
    const response = await fetch(pkg.repo)
        .catch(e => {
            p.log.error('Download Pkg Repo-Script error: ' + JSON.stringify(e))
            process.exit(0)
        })
    spin.stop('Pull Complete')
    let script = await response.text()
    await Bun.write(`${config.tmp}/tmp.sh`, script)

    spin.start('Executing Install Script')
    await new Promise<void>(resolve => {
        const proc = Bun.spawn(['sh',`tmp.sh`,`${config.home}/${pkg.label}`], {
            cwd: config.tmp,
            onExit() {
                resolve()
            }
        })
        proc.unref()
        process.on('exit',()=>{
            proc.kill(9)
        })
    })
    spin.stop('Executed Install Script')
    p.outro('Installed')
}


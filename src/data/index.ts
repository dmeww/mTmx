import type {Config, Pkg} from "../types";
import * as p from '@clack/prompts'

export const lastExit = {label: 'Exit', value: -1, hint: 'Exit...'} as Pkg

export const loadData = async (): Promise<Pkg[]> => {
    try {
        if (await Bun.file(`${config.home}/repo.json`).exists()) {
            let file = Bun.file(`${config.home}/repo.json`)
            let data = await file.text()
            data = JSON.parse(data)
            return [lastExit, ...data] as Pkg[]
        } else {
            p.log.warning('Repo File Not Exists: please run update command')
            return [lastExit] as Pkg[]
        }
    } catch (err) {
        p.log.warning('Repo File Parse Error: please run update command')
        return [lastExit] as Pkg[]
    }
}

// Only For Linux & Termux
// TODO My:=>
//      LinuxAt:    /var/opt/mtmx
//      TermuxAt:   /data/data/com.termux/files/usr/var/opt/mtmx
// TODO Please set a Absolute Path
export const config: Config = {
    home: '.',
    tmp: '.'
}

/**
 * Dir
 * - Home
 *  - repo.json
 *  - PkgA
 *   - pm2.ecosystem.js
 *   - Software Files
 *  - PkgB
 *   - pm2.ecosystem.js
 *   - Software Files
 * - Temp
 */

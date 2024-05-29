import * as p from '@clack/prompts'
import {config} from "../data";

export const updateRepo = async (URL: string) => {
    const response = await fetch(URL).catch(e => {
        p.log.error('Error while loading URL')
        process.exit(0)
    })

    if (!response.ok) {
        p.log.error('Download JSON Repo Failed!')
    }

    const data = await response.text().catch(e => {
        console.log(e,JSON.stringify(e))
        p.log.error('Error while parsing data, maybe it\'not a json')
        process.exit(0)
    })

    await Bun.write(`${config.home}/repo.json`, data)
}
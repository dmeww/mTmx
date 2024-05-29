import * as p from '@clack/prompts';
import {loadData} from "../data";
import type {Pkg} from "../types";
import install from "./install.ts";


const listPackages = async () => {
    let pkgs: Pkg[] = []
    pkgs = await loadData()
    let index = await p.select({
        message: `Packages List`,
        options: pkgs,
        initialValue: 0,
        maxItems: 10
    }).then(result => {
        if (typeof result === 'number' && result !== -1) return result
        p.log.success('Bye')
        process.exit(0)
    })
    let pkg = pkgs.filter(pkg => pkg.value === index)[0]
    await p.confirm({
        message: `Are you sure to install [${pkg.label}] ?\n< It will override the pkg which have same PkgName. >`,
        active: 'Yes',
        inactive: 'No',
        initialValue: true
    }).then(result => {
        if (typeof result === 'boolean' && result) return result
        p.log.success('Bye')
        process.exit(0)
    })

    p.log.success(`Preparing [${pkg.label}] `)
    await install(pkg)
}

export default listPackages

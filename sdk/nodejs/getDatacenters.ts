// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Provides a list of available Hetzner Cloud Datacenters.
 * This resource may be useful to create highly available infrastructure, distributed across several datacenters.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as hcloud from "@pulumi/hcloud";
 *
 * const ds = pulumi.output(hcloud.getDatacenters({ async: true }));
 * const workers: hcloud.Server[] = [];
 * for (let i = 0; i < 3; i++) {
 *     workers.push(new hcloud.Server(`workers-${i}`, {
 *         datacenter: ds.apply(ds => ds.names[i]),
 *         image: "debian-9",
 *         serverType: "cx31",
 *     }));
 * }
 * ```
 */
export function getDatacenters(args?: GetDatacentersArgs, opts?: pulumi.InvokeOptions): Promise<GetDatacentersResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("hcloud:index/getDatacenters:getDatacenters", {
        "datacenterIds": args.datacenterIds,
    }, opts);
}

/**
 * A collection of arguments for invoking getDatacenters.
 */
export interface GetDatacentersArgs {
    readonly datacenterIds?: string[];
}

/**
 * A collection of values returned by getDatacenters.
 */
export interface GetDatacentersResult {
    readonly datacenterIds?: string[];
    readonly descriptions: string[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly names: string[];
}

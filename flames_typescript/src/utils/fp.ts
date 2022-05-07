import * as TE from "fp-ts/lib/TaskEither";
import { pipe } from "fp-ts/lib/function"

export const makeTE = <A = any>(lazyFn: () => Promise<A>) => TE.tryCatch(() => lazyFn(), reason => Error(String(reason)))

export const fpPipe = pipe;
export const TEbindTo = TE.bindTo;
export const TEbindW = TE.bindW;
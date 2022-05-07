import { fpPipe, makeTE, TEbindTo, TEbindW } from "../utils/fp"
import * as TE from "fp-ts/lib/TaskEither"
import { FlameT } from "../types";
import { FlamesMap } from "./constants";

const makeValidNames = async (name: string) => name.replace(" ", "").toLowerCase();

export const makeValidNamesTE = (name: string) => makeTE(() => makeValidNames(name))

const getFlamesLength = async (name1: string, name2: string): Promise<number> => {
    const splitedName1 = name1.split("");
    const splitedName2 = name2.split("");
    let convertedArray = splitedName1.reduce((a: FlameT, b: string) => {
        let index = splitedName2.indexOf(b);
        if (splitedName2.indexOf(b) == -1) {
            a.firstNameAfterRejection.push(b)
            return a
        } else {
            splitedName2.splice(index, 1)
            return {
                firstNameAfterRejection: a.firstNameAfterRejection,
                secondNameAfterRejection: splitedName2
            }
        }
    }, { firstNameAfterRejection: [], secondNameAfterRejection: [] });
    return convertedArray.firstNameAfterRejection.concat(convertedArray.secondNameAfterRejection).length
}

export const getFlamesLengthTE = (name1: string, name2: string) => makeTE(() => getFlamesLength(name1, name2))

const f = (flames: string[], startNumber: number, length: number) => {
    if (flames.length == 1) {
        return flames[0];
    }
    let indexToRemove = length % flames.length;
    delete flames[indexToRemove]
    flames = flames.filter(e => e);
    return f(flames, startNumber, length);
}

const performFlames = (length: number) : TE.TaskEither<Error, string>=> {
    let flames = ["f", "l", "a", "m", "e", "s"];
    let key = f(flames, 0, length)
    return FlamesMap.get(key) ? TE.right(FlamesMap.get(key)) : TE.left(new Error("Value is not declared."));
}

export const flames = (box1Name: string, box2Name: string) => fpPipe(
    makeValidNamesTE(box1Name),
    TE.bindTo("firstName"),
    TE.bindW("secondName", () => makeValidNamesTE(box2Name)),
    TE.bindW("flames", ({ firstName, secondName }) => getFlamesLengthTE(firstName, secondName)),
    TE.bindW("lengths", ({ firstName, secondName }) => TE.right({ length: { firstName: firstName.length, secondName: secondName.length } })),
    TE.bindW("result", ({ flames }) => performFlames(flames))
)

// ts-node src // RUNCOMMAND
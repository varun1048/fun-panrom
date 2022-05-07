type ErrorT = Error & {
    code ?: string
}

type NumberOrString<T> = T extends string ? {
    name : string
} : T extends number ? {
    age : number
} : never;

type ErrorS<T> = T extends "Internal_server_error" ? {
    type : "Internal_server_error",
    Error : Error
} : T extends "NOT_FOUND" ? {
    type : "NOT_FOUND",
    message : "Location not found.",
    Error : Error
} : never 

type MessageT = "Test1" | "Test2" | "Test3"

const test : ErrorS<"NOT_FOUND"> = {
   type : "NOT_FOUND",
   message : "Location not found.",
   Error : new Error("")
};

const makeError = <A extends MessageT>(message : A) => {
    let err : ErrorT = new Error(message);
    err.code = "Error";
    return err;
}

makeError("Test2")
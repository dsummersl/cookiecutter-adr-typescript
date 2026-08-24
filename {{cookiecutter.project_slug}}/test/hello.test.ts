import { describe, it, expect } from "vitest";

import { world } from "../src/hello.js";

describe("world", () => {
  it("says hello world", () => {
    expect(world()).toBe("hello world");
  });
});
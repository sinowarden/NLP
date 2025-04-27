
# 这是一个自动生成的Python文件
def hello_world():
    print("Hello, world! Time is 'Fri Nov 10 15:10:23 2023'")


if __name__ == "__main__":
    hello_world()
    a = 1
            // Licensed under the Apache License, Version 2.0 (the 'License');
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an 'AS IS' BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

goog.module('myphysicslab.test.DoNothingTest');

const CollisionAdvance = goog.require('myphysicslab.lab.model.CollisionAdvance');
const CollisionHandling = goog.require('myphysicslab.lab.engine2D.CollisionHandling');
const ConstantForceLaw = goog.require('myphysicslab.lab.model.ConstantForceLaw');
const ContactSim = goog.require('myphysicslab.lab.engine2D.ContactSim');
const CoordType = goog.require('myphysicslab.lab.model.CoordType');
const DampingLaw = goog.require('myphysicslab.lab.model.DampingLaw');
const DoNothingApp = goog.require('myphysicslab.sims.engine2D.DoNothingApp');
const DoubleRect = goog.require('myphysicslab.lab.util.DoubleRect');
const Engine2DTestRig = goog.require('myphysicslab.test.Engine2DTestRig');
const ExtraAccel = goog.require('myphysicslab.lab.engine2D.ExtraAccel');
const Force = goog.require('myphysicslab.lab.model.Force');
const RandomLCG = goog.require('myphysicslab.lab.util.RandomLCG');
const RotatingTestForce = goog.require('myphysicslab.sims.engine2D.RotatingTestForce');
const RungeKutta = goog.require('myphysicslab.lab.model.RungeKutta');
const TestRig = goog.require('myphysicslab.test.TestRig');
const Util = goog.require('myphysicslab.lab.util.Util');
const Vector = goog.require('myphysicslab.lab.util.Vector');

const assertTrue = v => TestRig.assertTrue(v);
const assertLessThan = (v, l) => TestRig.assertLessThan(v, l);
const makeVars = n => Engine2DTestRig.makeVars(n);
const schedule = testFunc => TestRig.schedule(testFunc);
const setBodyVars = (sim, vars, i, x, vx, y, vy, w, vw) =>
    Engine2DTestRig.setBodyVars(sim, vars, i, x, vx, y, vy, w, vw);
const setTestName = nm => Engine2DTestRig.setTestName(nm);

/** Defines tests involving {@link DoNothingApp}.
*/
class DoNothingTest {
/**
@private
*/
constructor() { throw ''; };

static test() {
  schedule(DoNothingTest.do_nothing_grinder_test1);
  schedule(DoNothingTest.do_nothing_grinder_test1b);
  schedule(DoNothingTest.do_nothing_grinder_test2);
  schedule(DoNothingTest.do_nothing_variable_test);
  schedule(DoNothingTest.do_nothing_error);
};
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an 'AS IS' BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

goog.module('myphysicslab.test.DoNothingTest');

const CollisionAdvance = goog.require('myphysicslab.lab.model.CollisionAdvance');
const CollisionHandling = goog.require('myphysicslab.lab.engine2D.CollisionHandling');
const ConstantForceLaw = goog.require('myphysicslab.lab.model.ConstantForceLaw');
const ContactSim = goog.require('myphysicslab.lab.engine2D.ContactSim');
const CoordType = goog.require('myphysicslab.lab.model.CoordType');
const DampingLaw = goog.require('myphysicslab.lab.model.DampingLaw');
const DoNothingApp = goog.require('myphysicslab.sims.engine2D.DoNothingApp');
const DoubleRect = goog.require('myphysicslab.lab.util.DoubleRect');
const Engine2DTestRig = goog.require('myphysicslab.test.Engine2DTestRig');
const ExtraAccel = goog.require('myphysicslab.lab.engine2D.ExtraAccel');
const Force = goog.require('myphysicslab.lab.model.Force');
const RandomLCG = goog.require('myphysicslab.lab.util.RandomLCG');
const RotatingTestForce = goog.require('myphysicslab.sims.engine2D.RotatingTestForce');
const RungeKutta = goog.require('myphysicslab.lab.model.RungeKutta');
const TestRig = goog.require('myphysicslab.test.TestRig');
const Util = goog.require('myphysicslab.lab.util.Util');
const Vector = goog.require('myphysicslab.lab.util.Vector');

const assertTrue = v => TestRig.assertTrue(v);
const assertLessThan = (v, l) => TestRig.assertLessThan(v, l);
const makeVars = n => Engine2DTestRig.makeVars(n);
const schedule = testFunc => TestRig.schedule(testFunc);
const setBodyVars = (sim, vars, i, x, vx, y, vy, w, vw) =>
    Engine2DTestRig.setBodyVars(sim, vars, i, x, vx, y, vy, w, vw);
const setTestName = nm => Engine2DTestRig.setTestName(nm);

/** Defines tests involving {@link DoNothingApp}.
*/
class DoNothingTest {
/**
@private
*/
constructor() { throw ''; };

static test() {
  schedule(DoNothingTest.do_nothing_grinder_test1);
  schedule(DoNothingTest.do_nothing_grinder_test1b);
  schedule(DoNothingTest.do_nothing_grinder_test2);
  schedule(DoNothingTest.do_nothing_variable_test);
  schedule(DoNothingTest.do_nothing_error);
};

/** DoNothingApp with variable rotating force on handle.
@param {!ContactSim} sim
@param {!CollisionAdvance} advance
@export
*/
static do_nothing_variable_setup(sim, advance) {
  sim.addForceLaw(new DampingLaw(0.05, 0.15, sim.getSimList()));
  sim.setDistanceTol(0.01);
  sim.setVelocityTol(0.5);
  sim.setCollisionHandling(CollisionHandling.SERIAL_GROUPED_LASTPASS);
  sim.setShowForces(false);
  sim.setCollisionAccuracy(0.6);
  advance.setDiffEqSolver(new RungeKutta(sim));
  sim.setExtraAccel(ExtraAccel.VELOCITY);
  advance.setJointSmallImpacts(true);
  advance.setTimeStep(0.025);
  DoNothingApp.setup(sim, /*tightFit=*/true);
  sim.setElasticity(0.8);
  sim.setSimRect(new DoubleRect(-5, -5, 5, 5));
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an 'AS IS' BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

goog.module('myphysicslab.test.DoNothingTest');

const CollisionAdvance = goog.require('myphysicslab.lab.model.CollisionAdvance');
const CollisionHandling = goog.require('myphysicslab.lab.engine2D.CollisionHandling');
const ConstantForceLaw = goog.require('myphysicslab.lab.model.ConstantForceLaw');
const ContactSim = goog.require('myphysicslab.lab.engine2D.ContactSim');
const CoordType = goog.require('myphysicslab.lab.model.CoordType');
const DampingLaw = goog.require('myphysicslab.lab.model.DampingLaw');
const DoNothingApp = goog.require('myphysicslab.sims.engine2D.DoNothingApp');
const DoubleRect = goog.require('myphysicslab.lab.util.DoubleRect');
const Engine2DTestRig = goog.require('myphysicslab.test.Engine2DTestRig');
const ExtraAccel = goog.require('myphysicslab.lab.engine2D.ExtraAccel');
const Force = goog.require('myphysicslab.lab.model.Force');
const RandomLCG = goog.require('myphysicslab.lab.util.RandomLCG');
const RotatingTestForce = goog.require('myphysicslab.sims.engine2D.RotatingTestForce');
const RungeKutta = goog.require('myphysicslab.lab.model.RungeKutta');
const TestRig = goog.require('myphysicslab.test.TestRig');
const Util = goog.require('myphysicslab.lab.util.Util');
const Vector = goog.require('myphysicslab.lab.util.Vector');

const assertTrue = v => TestRig.assertTrue(v);
const assertLessThan = (v, l) => TestRig.assertLessThan(v, l);
const makeVars = n => Engine2DTestRig.makeVars(n);
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an 'AS IS' BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

goog.module('myphysicslab.test.DoNothingTest');

const CollisionAdvance = goog.require('myphysicslab.lab.model.CollisionAdvance');
const CollisionHandling = goog.require('myphysicslab.lab.engine2D.CollisionHandling');
const ConstantForceLaw = goog.require('myphysicslab.lab.model.ConstantForceLaw');
const ContactSim = goog.require('myphysicslab.lab.engine2D.ContactSim');
const CoordType = goog.require('myphysicslab.lab.model.CoordType');
const DampingLaw = goog.require('myphysicslab.lab.model.DampingLaw');
const DoNothingApp = goog.require('myphysicslab.sims.engine2D.DoNothingApp');
const DoubleRect = goog.require('myphysicslab.lab.util.DoubleRect');
const Engine2DTestRig = goog.require('myphysicslab.test.Engine2DTestRig');
const ExtraAccel = goog.require('myphysicslab.lab.engine2D.ExtraAccel');
const Force = goog.require('myphysicslab.lab.model.Force');
const RandomLCG = goog.require('myphysicslab.lab.util.RandomLCG');
const RotatingTestForce = goog.require('myphysicslab.sims.engine2D.RotatingTestForce');
const RungeKutta = goog.require('myphysicslab.lab.model.RungeKutta');
const TestRig = goog.require('myphysicslab.test.TestRig');
const Util = goog.require('myphysicslab.lab.util.Util');
const Vector = goog.require('myphysicslab.lab.util.Vector');
// distributed under the License is distributed on an 'AS IS' BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

goog.module('myphysicslab.test.DoNothingTest');

const CollisionAdvance = goog.require('myphysicslab.lab.model.CollisionAdvance');
const CollisionHandling = goog.require('myphysicslab.lab.engine2D.CollisionHandling');
const ConstantForceLaw = goog.require('myphysicslab.lab.model.ConstantForceLaw');
const ContactSim = goog.require('myphysicslab.lab.engine2D.ContactSim');
const CoordType = goog.require('myphysicslab.lab.model.CoordType');
const DampingLaw = goog.require('myphysicslab.lab.model.DampingLaw');
const DoNothingApp = goog.require('myphysicslab.sims.engine2D.DoNothingApp');
const DoubleRect = goog.require('myphysicslab.lab.util.DoubleRect');
const Engine2DTestRig = goog.require('myphysicslab.test.Engine2DTestRig');
const ExtraAccel = goog.require('myphysicslab.lab.engine2D.ExtraAccel');
const Force = goog.require('myphysicslab.lab.model.Force');
const RandomLCG = goog.require('myphysicslab.lab.util.RandomLCG');
const RotatingTestForce = goog.require('myphysicslab.sims.engine2D.RotatingTestForce');
const RungeKutta = goog.require('myphysicslab.lab.model.RungeKutta');
const TestRig = goog.require('myphysicslab.test.TestRig');
const Util = goog.require('myphysicslab.lab.util.Util');
const Vector = goog.require('myphysicslab.lab.util.Vector');

const assertTrue = v => TestRig.assertTrue(v);
const assertLessThan = (v, l) => TestRig.assertLessThan(v, l);
const makeVars = n => Engine2DTestRig.makeVars(n);
const schedule = testFunc => TestRig.schedule(testFunc);
const setBodyVars = (sim, vars, i, x, vx, y, vy, w, vw) =>
    Engine2DTestRig.setBodyVars(sim, vars, i, x, vx, y, vy, w, vw);
const setTestName = nm => Engine2DTestRig.setTestName(nm);
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an 'AS IS' BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

goog.module('myphysicslab.test.DoNothingTest');

const CollisionAdvance = goog.require('myphysicslab.lab.model.CollisionAdvance');
const CollisionHandling = goog.require('myphysicslab.lab.engine2D.CollisionHandling');
const ConstantForceLaw = goog.require('myphysicslab.lab.model.ConstantForceLaw');
const ContactSim = goog.require('myphysicslab.lab.engine2D.ContactSim');
const CoordType = goog.require('myphysicslab.lab.model.CoordType');
const DampingLaw = goog.require('myphysicslab.lab.model.DampingLaw');
const DoNothingApp = goog.require('myphysicslab.sims.engine2D.DoNothingApp');
const DoubleRect = goog.require('myphysicslab.lab.util.DoubleRect');
const Engine2DTestRig = goog.require('myphysicslab.test.Engine2DTestRig');
const ExtraAccel = goog.require('myphysicslab.lab.engine2D.ExtraAccel');
const Force = goog.require('myphysicslab.lab.model.Force');
const RandomLCG = goog.require('myphysicslab.lab.util.RandomLCG');
const RotatingTestForce = goog.require('myphysicslab.sims.engine2D.RotatingTestForce');
const RungeKutta = goog.require('myphysicslab.lab.model.RungeKutta');
const TestRig = goog.require('myphysicslab.test.TestRig');
const Util = goog.require('myphysicslab.lab.util.Util');
const Vector = goog.require('myphysicslab.lab.util.Vector');

const assertTrue = v => TestRig.assertTrue(v);
const assertLessThan = (v, l) => TestRig.assertLessThan(v, l);
const makeVars = n => Engine2DTestRig.makeVars(n);
const schedule = testFunc => TestRig.schedule(testFunc);
const setBodyVars = (sim, vars, i, x, vx, y, vy, w, vw) =>
    Engine2DTestRig.setBodyVars(sim, vars, i, x, vx, y, vy, w, vw);
const setTestName = nm => Engine2DTestRig.setTestName(nm);

/** Defines tests involving {@link DoNothingApp}.
*/
class DoNothingTest {
/**
@private
*/
constructor() { throw ''; };

static test() {
  schedule(DoNothingTest.do_nothing_grinder_test1);
  schedule(DoNothingTest.do_nothing_grinder_test1b);
  schedule(DoNothingTest.do_nothing_grinder_test2);
  schedule(DoNothingTest.do_nothing_variable_test);
  schedule(DoNothingTest.do_nothing_error);
};

/** DoNothingApp with variable rotating force on handle.
@param {!ContactSim} sim
@param {!CollisionAdvance} advance
@export
*/
static do_nothing_variable_setup(sim, advance) {
  sim.addForceLaw(new DampingLaw(0.05, 0.15, sim.getSimList()));
  sim.setDistanceTol(0.01);
  sim.setVelocityTol(0.5);
  sim.setCollisionHandling(CollisionHandling.SERIAL_GROUPED_LASTPASS);
  sim.setShowForces(false);
  sim.setCollisionAccuracy(0.6);
  advance.setDiffEqSolver(new RungeKutta(sim));
  sim.setExtraAccel(ExtraAccel.VELOCITY);
  advance.setJointSmallImpacts(true);
  advance.setTimeStep(0.025);
  DoNothingApp.setup(sim, /*tightFit=*/true);
  sim.setElasticity(0.8);
  sim.setSimRect(new DoubleRect(-5, -5, 5, 5));
  // add a rotating force turning the handle
  const handle = sim.getBody('handle');
  sim.addForceLaw(new RotatingTestForce(sim, handle, new Vector(0, -3),
    /*magnitude=*/2, /*rotation_rate=*/0.3));
};

/** Test of DoNothingApp with variable rotating force on handle.
This test has many redundant contacts, which activates code in ComputeForces
that looks for singular matrices.
* @return {undefined}
*/
static do_nothing_variable_test() {
  setTestName(DoNothingTest.groupName+'do_nothing_variable_test');
  const sim = new ContactSim();
  const advance = new CollisionAdvance(sim);
  DoNothingTest.do_nothing_variable_setup(sim, advance);
  const vars = makeVars((4 + 3)*6);
  Engine2DTestRig.setBodyVars(sim, vars, 0, -2.350918, -1.4252083, 0.2181222, -0.3159406, -7.2797567, -0.9370725);
  Engine2DTestRig.setBodyVars(sim, vars, 1, 0, -0, 1.7390377, -2.5189213, 3.1415927, -0);
  Engine2DTestRig.setBodyVars(sim, vars, 2, -2.688075, -1.6296046, -0, 0, 1.5707963, 0);
  setBodyVars(sim, vars, 3, 2.507, 0, 2.507, 0, 0, 0);
  setBodyVars(sim, vars, 4, 2.507, 0, -2.507, 0, 0, 0);
  setBodyVars(sim, vars, 5, -2.507, 0, 2.507, 0, 0, 0);
  setBodyVars(sim, vars, 6, -2.507, 0, -2.507, 0, 0, 0);
// Licensed under the Apache License, Version 2.0 (the 'License');
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an 'AS IS' BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

goog.module('myphysicslab.test.DoNothingTest');

const CollisionAdvance = goog.require('myphysicslab.lab.model.CollisionAdvance');
const CollisionHandling = goog.require('myphysicslab.lab.engine2D.CollisionHandling');
const ConstantForceLaw = goog.require('myphysicslab.lab.model.ConstantForceLaw');
const ContactSim = goog.require('myphysicslab.lab.engine2D.ContactSim');
const CoordType = goog.require('myphysicslab.lab.model.CoordType');
const DampingLaw = goog.require('myphysicslab.lab.model.DampingLaw');
const DoNothingApp = goog.require('myphysicslab.sims.engine2D.DoNothingApp');
const DoubleRect = goog.require('myphysicslab.lab.util.DoubleRect');
const Engine2DTestRig = goog.require('myphysicslab.test.Engine2DTestRig');
const ExtraAccel = goog.require('myphysicslab.lab.engine2D.ExtraAccel');
const Force = goog.require('myphysicslab.lab.model.Force');
const RandomLCG = goog.require('myphysicslab.lab.util.RandomLCG');
const RotatingTestForce = goog.require('myphysicslab.sims.engine2D.RotatingTestForce');
const RungeKutta = goog.require('myphysicslab.lab.model.RungeKutta');
const TestRig = goog.require('myphysicslab.test.TestRig');
const Util = goog.require('myphysicslab.lab.util.Util');
const Vector = goog.require('myphysicslab.lab.util.Vector');

const assertTrue = v => TestRig.assertTrue(v);
const assertLessThan = (v, l) => TestRig.assertLessThan(v, l);
const makeVars = n => Engine2DTestRig.makeVars(n);
const schedule = testFunc => TestRig.schedule(testFunc);
const setBodyVars = (sim, vars, i, x, vx, y, vy, w, vw) =>
    Engine2DTestRig.setBodyVars(sim, vars, i, x, vx, y, vy, w, vw);
const setTestName = nm => Engine2DTestRig.setTestName(nm);

/** Defines tests involving {@link DoNothingApp}.
*/
class DoNothingTest {
/**
@private
*/
constructor() { throw ''; };

static test() {
  schedule(DoNothingTest.do_nothing_grinder_test1);
  schedule(DoNothingTest.do_nothing_grinder_test1b);
  schedule(DoNothingTest.do_nothing_grinder_test2);
  schedule(DoNothingTest.do_nothing_variable_test);
  schedule(DoNothingTest.do_nothing_error);
};

/** DoNothingApp with variable rotating force on handle.
@param {!ContactSim} sim
@param {!CollisionAdvance} advance
@export
*/
static do_nothing_variable_setup(sim, advance) {
  sim.addForceLaw(new DampingLaw(0.05, 0.15, sim.getSimList()));
  sim.setDistanceTol(0.01);
  sim.setVelocityTol(0.5);
  sim.setCollisionHandling(CollisionHandling.SERIAL_GROUPED_LASTPASS);
  sim.setShowForces(false);
  sim.setCollisionAccuracy(0.6);
  advance.setDiffEqSolver(new RungeKutta(sim));
  sim.setExtraAccel(ExtraAccel.VELOCITY);
  advance.setJointSmallImpacts(true);
  advance.setTimeStep(0.025);
  DoNothingApp.setup(sim, /*tightFit=*/true);
  sim.setElasticity(0.8);
  sim.setSimRect(new DoubleRect(-5, -5, 5, 5));
  // add a rotating force turning the handle
  const handle = sim.getBody('handle');
  sim.addForceLaw(new RotatingTestForce(sim, handle, new Vector(0, -3),
    /*magnitude=*/2, /*rotation_rate=*/0.3));
};

/** Test of DoNothingApp with variable rotating force on handle.
This test has many redundant contacts, which activates code in ComputeForces
that looks for singular matrices.
* @return {undefined}
*/
static do_nothing_variable_test() {
  setTestName(DoNothingTest.groupName+'do_nothing_variable_test');
  const sim = new ContactSim();

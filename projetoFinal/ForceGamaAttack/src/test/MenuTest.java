package test;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

import static org.hamcrest.CoreMatchers.instanceOf;

import scenes.menu.ConfigState;
import scenes.menu.CreditState;
import scenes.menu.ExitState;
import scenes.menu.Menu;
import scenes.menu.StartState;
import scenes.spaceShipMenu.SpaceShipMenuScene;

public class MenuTest {
	private Menu menu;
	private StartState startState;
	private ConfigState configState;
	private ExitState exitState;
	private CreditState creditState;
	
	@Before
	public void setUp() throws Exception{
		startState = new StartState();
		configState = new ConfigState();
		exitState = new ExitState();
		creditState = new CreditState();
	}
	
	@Test
	public void testMenuConfig() {
		menu = new Menu(configState);
		assertEquals(menu.getOrdinal(), configState.getOrdinal());
	}
	
	@Test
	public void testMenuStart() {
		menu = new Menu(startState);
		assertEquals(menu.getOrdinal(), startState.getOrdinal());
	}
	
	@Test
	public void testMenuExit() {
		menu = new Menu(exitState);
		assertEquals(menu.getOrdinal(), exitState.getOrdinal());
	}
	
	@Test
	public void testMenuCredit() {
		menu = new Menu(creditState);
		assertEquals(menu.getOrdinal(), creditState.getOrdinal());
	}
	
	@Test
	public void testSetState() {
		menu = new Menu(startState);
		menu.setState(configState);
		assertEquals(menu.getState(), configState);
	}

	@Test
	public void testGetState() {
		menu = new Menu(startState);
		assertEquals(menu.getState(), startState);
	}


	@Test
	public void testGetOrdinal() {
		menu = new Menu(startState);
		assertEquals(menu.getOrdinal(), startState.getOrdinal());
	}

	@Test
	public void testGetScene() {
		menu = new Menu(startState);
		assertThat(menu.getScene(), instanceOf(SpaceShipMenuScene.class));
	}

}
